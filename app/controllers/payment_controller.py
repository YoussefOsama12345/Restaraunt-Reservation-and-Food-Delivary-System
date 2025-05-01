"""
Payment Controller

Handles requests related to payment operations such as initiating, confirming,
and retrieving payment status.

Delegates business logic to the `payment_service` module.

Roles:
- User: Initiate and confirm payments, retrieve status
- Public: Webhook callbacks from payment providers
"""

from fastapi import Depends, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.payment import PaymentInitiate, PaymentStatus, PaymentConfirm
from app.services import payment_service


async def initiate_payment_controller(
    payment_data: PaymentInitiate,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends()
) -> dict:
    """
    Initiate a new payment session for an order.
    Role: User
    """
    try:
        payment_dict = payment_data.dict()
        result = await payment_service.initiate_payment(payment_dict, current_user.id, db)
        
        # Ensure payment_details is properly formatted for Pydantic
        if 'payment_details' in result and result['payment_details'] is None:
            result['payment_details'] = {}
        
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_payment_status_controller(
    payment_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends()
) -> dict:
    """
    Retrieve the current status of a specific payment.
    Role: User
    """
    try:
        result = await payment_service.get_payment_status(payment_id, current_user.id, db)
        
        # Ensure payment_details is properly formatted for Pydantic
        if 'payment_details' in result and result['payment_details'] is None:
            result['payment_details'] = {}
        
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def confirm_payment_controller(
    payment_id: int,
    confirmation_data: PaymentConfirm,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends()
) -> dict:
    """
    Confirm a payment after front-end processing.
    Role: User
    """
    try:
        confirm_dict = confirmation_data.dict()
        result = await payment_service.confirm_payment(payment_id, confirm_dict, current_user.id, db)
        
        # Ensure payment_details is properly formatted for Pydantic
        if 'payment_details' in result and result['payment_details'] is None:
            result['payment_details'] = {}
        
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def payment_webhook_controller(
    request: Request,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Handle payment webhook events from payment providers.
    Role: Public (no auth required)
    """
    try:
        return await payment_service.handle_webhook(request, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
