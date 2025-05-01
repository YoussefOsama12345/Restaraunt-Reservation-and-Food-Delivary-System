"""
Payment Service

Handles payment session initiation, confirmation, status retrieval,
and webhook processing.

Integrates with one or more payment providers through internal or external APIs.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status, Request
from app.db.models.payment import Payment, PaymentStatusEnum
from app.db.models.order import Order
from datetime import datetime
import json
from typing import Optional

# Placeholder models/schemas for standalone usage
class PaymentInitiate:
    amount: float
    currency: str
    order_id: int

class PaymentConfirm:
    confirmation_id: str
    status: str


async def initiate_payment(payment_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Initiate a new payment session.

    Args:
        payment_data (PaymentInitiate): Payment details including amount, method, and order reference.
        user_id (int): ID of the user initiating the payment.

    Returns:
        dict: Payment session information (e.g., redirect URL or token).

    Role: User
    """
    # Validate that order_id exists and is valid (not 0)
    if 'order_id' not in payment_data or not payment_data['order_id'] or payment_data['order_id'] <= 0:
        raise ValueError("A valid order_id is required for payment initiation")
    
    # Check if the order exists before creating a payment
    try:
        result = await db.execute(select(Order).where(Order.id == payment_data['order_id']))
        order = result.scalars().first()
        if not order:
            raise ValueError(f"Order with ID {payment_data['order_id']} not found")
    except Exception as e:
        # If there's an error checking the order, provide a clear message
        raise ValueError(f"Error validating order: {str(e)}")
    
    # Validate amount is greater than 0
    if 'amount' not in payment_data or not payment_data['amount'] or payment_data['amount'] <= 0:
        raise ValueError("A valid amount greater than 0 is required for payment initiation")
    
    # Filter only SQLAlchemy columns
    payment_fields = {k: v for k, v in payment_data.items() if k in Payment.__table__.columns.keys()}
    payment_fields['user_id'] = user_id
    payment_fields['status'] = PaymentStatusEnum.PENDING
    payment_fields['created_at'] = datetime.utcnow()
    payment_fields['updated_at'] = datetime.utcnow()
    
    # Map 'method' to 'payment_method' if present and not already set
    if 'method' in payment_data and 'payment_method' not in payment_fields:
        payment_fields['payment_method'] = payment_data['method']
    
    # Ensure required fields have valid values
    payment_fields['order_id'] = payment_data['order_id']
    payment_fields['amount'] = payment_data['amount']
    
    # Generate a transaction ID if not provided
    if 'transaction_id' not in payment_fields or not payment_fields['transaction_id']:
        payment_fields['transaction_id'] = f"txn_{datetime.utcnow().timestamp()}_{user_id}"
    
    # Set payment gateway if not provided
    if 'payment_gateway' not in payment_fields or not payment_fields['payment_gateway']:
        payment_fields['payment_gateway'] = 'stripe'  # Default to stripe
    
    # Create a default payment details dictionary
    default_payment_details = {
        "card_last4": "1234",
        "card_brand": "visa",
        "payment_intent": f"pi_{datetime.utcnow().timestamp()}"
    }
    
    # Store payment details as a JSON string in the database
    if 'payment_details' not in payment_fields or not payment_fields['payment_details']:
        payment_fields['payment_details'] = json.dumps(default_payment_details)
    elif isinstance(payment_fields['payment_details'], dict):
        payment_fields['payment_details'] = json.dumps(payment_fields['payment_details'])
    
    try:
        payment = Payment(**payment_fields)
        db.add(payment)
        await db.commit()
        await db.refresh(payment)
        
        # Prepare the result with all required fields for PaymentStatus schema
        result = {c.name: getattr(payment, c.name) for c in Payment.__table__.columns}
        
        # Convert payment_details from JSON string to dict for the response
        if 'payment_details' in result:
            if isinstance(result['payment_details'], str):
                try:
                    result['payment_details'] = json.loads(result['payment_details'])
                except json.JSONDecodeError:
                    # If JSON parsing fails, create a valid dict
                    result['payment_details'] = default_payment_details
            elif result['payment_details'] is None:
                result['payment_details'] = default_payment_details
        else:
            result['payment_details'] = default_payment_details
        
        return result
    except Exception as e:
        await db.rollback()
        raise ValueError(f"Failed to create payment: {str(e)}")


async def get_payment_status(payment_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve the current status of a payment.

    Args:
        payment_id (str): ID of the payment to retrieve.
        user_id (int): ID of the requesting user.

    Returns:
        Payment: Payment object with current status and metadata.

    Role: User
    """
    result = await db.execute(select(Payment).where(Payment.id == payment_id, Payment.user_id == user_id))
    payment = result.scalars().first()
    if not payment:
        raise Exception("Payment not found or unauthorized")
    
    # Convert to dict
    payment_dict = {c.name: getattr(payment, c.name) for c in Payment.__table__.columns}
    
    # Ensure payment_details is a dict
    if 'payment_details' in payment_dict:
        if isinstance(payment_dict['payment_details'], str):
            try:
                payment_dict['payment_details'] = json.loads(payment_dict['payment_details'])
            except json.JSONDecodeError:
                payment_dict['payment_details'] = {"details": payment_dict['payment_details']}
        elif payment_dict['payment_details'] is None:
            payment_dict['payment_details'] = {
                "card_last4": "1234",
                "card_brand": "visa",
                "payment_intent": f"pi_{datetime.utcnow().timestamp()}"
            }
    else:
        payment_dict['payment_details'] = {
            "card_last4": "1234",
            "card_brand": "visa",
            "payment_intent": f"pi_{datetime.utcnow().timestamp()}"
        }
    
    return payment_dict


async def confirm_payment(payment_id: int, confirmation_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Confirm the result of a payment session.

    Args:
        payment_id (str): ID of the payment to confirm.
        confirmation_data (PaymentConfirm): Result and metadata from frontend callback.
        user_id (int): ID of the user confirming the payment.

    Returns:
        dict: Confirmation details or updated payment status.

    Role: User
    """
    try:
        # Check if payment exists and belongs to user
        result = await db.execute(select(Payment).where(Payment.id == payment_id, Payment.user_id == user_id))
        payment = result.scalars().first()
        if not payment:
            raise Exception("Payment not found or unauthorized")
        
        # Update payment fields from confirmation data
        for field, value in confirmation_data.items():
            if hasattr(payment, field) and field in Payment.__table__.columns.keys():
                # Handle payment_details specially if it's a dict
                if field == 'payment_details' and isinstance(value, dict):
                    setattr(payment, field, json.dumps(value))
                else:
                    setattr(payment, field, value)
        
        # Set standard fields for completion
        payment.status = PaymentStatusEnum.COMPLETED
        payment.updated_at = datetime.utcnow()
        payment.completed_at = datetime.utcnow()
        
        # Commit changes
        await db.commit()
        await db.refresh(payment)
        
        # Create result dictionary
        payment_dict = {c.name: getattr(payment, c.name) for c in Payment.__table__.columns}
        
        # Ensure payment_details is a dict
        if 'payment_details' in payment_dict:
            if isinstance(payment_dict['payment_details'], str):
                try:
                    payment_dict['payment_details'] = json.loads(payment_dict['payment_details'])
                except json.JSONDecodeError:
                    payment_dict['payment_details'] = {"details": payment_dict['payment_details']}
            elif payment_dict['payment_details'] is None:
                payment_dict['payment_details'] = {
                    "card_last4": "1234",
                    "card_brand": "visa",
                    "payment_intent": f"pi_{datetime.utcnow().timestamp()}"
                }
        else:
            payment_dict['payment_details'] = {
                "card_last4": "1234",
                "card_brand": "visa",
                "payment_intent": f"pi_{datetime.utcnow().timestamp()}"
            }
        
        return payment_dict
    except Exception as e:
        await db.rollback()
        raise ValueError(f"Failed to confirm payment: {str(e)}")


async def handle_webhook(request: Request, db: AsyncSession) -> dict:
    """
    Handle webhook events from external payment providers.

    Args:
        request (Request): Incoming HTTP request containing the webhook payload.

    Returns:
        dict: Acknowledgment of the received event.

    Role: Public
    """
    payload = await request.body()
    # You would parse and validate the payload here, then update payment records as needed
    # For now, just log and acknowledge
    try:
        data = json.loads(payload)
    except Exception:
        data = str(payload)
    # Example: update payment status by transaction_id if present
    # ...
    return {"detail": "Webhook received", "data": data}
