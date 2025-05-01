from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PaymentInitiate(BaseModel):
    """
    Schema for initiating a payment.

    Attributes:
        order_id (int): The ID of the order for which the payment is being made.
        amount (float): The total amount to be charged for the order.
        currency (str): The currency in which the payment is made (default is "USD").
        method (str): The payment method used (e.g., "stripe", "paypal").
    """
    order_id: int
    amount: float
    currency: str = Field("USD", example="USD")
    method: str = Field(..., example="stripe")

    model_config = ConfigDict(from_attributes=True)


class PaymentConfirm(BaseModel):
    """
    Schema for confirming a payment.

    Attributes:
        payment_id (int): ID of the payment to confirm. Must be positive.
        order_id (int): ID of the order being paid for. Must be positive.
        user_id (int): ID of the user making the payment. Must be positive.
        payment_method (str): Method used for payment. Must be one of: credit_card, debit_card, net_banking, upi, wallet.
        transaction_id (str): Unique transaction ID from payment gateway.
        amount (float): Amount being paid. Must be greater than 0.
        currency (str): Currency code (e.g., USD, INR). Must be 3 characters.
        payment_status (str): Status of the payment. Must be one of: pending, completed, failed, refunded.
        payment_gateway (str): Payment gateway used (e.g., stripe, razorpay).
        payment_details (dict): Additional payment details from gateway.
        confirmation_code (Optional[str]): Confirmation code or reference number.
        notes (Optional[str]): Additional notes about the payment.
    """
    payment_id: int = Field(
        ...,
        gt=0,
        description="ID of the payment to confirm",
        example=101
    )
    order_id: int = Field(
        ...,
        gt=0,
        description="ID of the order being paid for",
        example=42
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user making the payment",
        example=15
    )
    payment_method: str = Field(
        ...,
        pattern="^(credit_card|debit_card|net_banking|upi|wallet)$",
        description="Method used for payment",
        example="credit_card"
    )
    transaction_id: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description="Unique transaction ID from payment gateway",
        example="txn_123456789"
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Amount being paid",
        example=42.99
    )
    currency: str = Field(
        "USD",
        pattern="^[A-Z]{3}$",
        description="Currency code",
        example="USD"
    )
    payment_status: str = Field(
        "pending",
        pattern="^(pending|completed|failed|refunded)$",
        description="Status of the payment",
        example="completed"
    )
    payment_gateway: str = Field(
        ...,
        pattern="^(stripe|razorpay|paypal|other)$",
        description="Payment gateway used",
        example="stripe"
    )
    payment_details: dict = Field(
        ...,
        description="Additional payment details from gateway",
        example={
            "card_last4": "4242",
            "card_brand": "visa",
            "payment_intent": "pi_123456789"
        }
    )
    confirmation_code: Optional[str] = Field(
        None,
        min_length=5,
        max_length=50,
        description="Confirmation code or reference number",
        example="CONF123456"
    )
    notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Additional notes about the payment",
        example="Payment processed successfully"
    )

    model_config = ConfigDict(from_attributes=True)


class PaymentStatus(BaseModel):
    """
    Schema for retrieving the status of a payment.

    Attributes:
        id (int): Unique identifier of the payment. Must be positive.
        order_id (int): ID of the order associated with the payment. Must be positive.
        user_id (int): ID of the user who made the payment. Must be positive.
        status (str): Current status of the payment. Must be one of: pending, completed, failed, refunded, partially_refunded.
        amount (float): Total amount of the payment. Must be greater than 0.
        currency (str): Currency code (e.g., USD, INR). Must be 3 characters.
        payment_method (str): Method used for payment. Must be one of: credit_card, debit_card, net_banking, upi, wallet.
        payment_gateway (str): Payment gateway used (e.g., stripe, razorpay).
        transaction_id (str): Unique transaction ID from payment gateway.
        created_at (datetime): When the payment was created.
        updated_at (datetime): When the payment was last updated.
        completed_at (Optional[datetime]): When the payment was completed.
        refunded_at (Optional[datetime]): When the payment was refunded.
        refund_amount (Optional[float]): Amount refunded if applicable.
        failure_reason (Optional[str]): Reason for payment failure if applicable.
        payment_details (dict): Additional payment details from gateway.
    """
    id: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the payment",
        example=101
    )
    order_id: int = Field(
        ...,
        gt=0,
        description="ID of the order associated with the payment",
        example=42
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user who made the payment",
        example=15
    )
    status: str = Field(
        ...,
        pattern="^(pending|completed|failed|refunded|partially_refunded)$",
        description="Current status of the payment",
        example="completed"
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Total amount of the payment",
        example=42.99
    )
    currency: str = Field(
        "USD",
        pattern="^[A-Z]{3}$",
        description="Currency code",
        example="USD"
    )
    payment_method: str = Field(
        ...,
        description="Method used for payment",
        example="credit_card"
    )
    payment_gateway: str = Field(
        ...,
        description="Payment gateway used",
        example="stripe"
    )
    transaction_id: str = Field(
        ...,
        description="Unique transaction ID from payment gateway",
        example="txn_123456789"
    )
    created_at: datetime = Field(
        ...,
        description="When the payment was created",
        example="2024-04-18T15:00:00Z"
    )
    updated_at: datetime = Field(
        ...,
        description="When the payment was last updated",
        example="2024-04-18T15:30:00Z"
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="When the payment was completed",
        example="2024-04-18T15:30:00Z"
    )
    refunded_at: Optional[datetime] = Field(
        None,
        description="When the payment was refunded",
        example="2024-04-18T16:00:00Z"
    )
    refund_amount: Optional[float] = Field(
        None,
        ge=0,
        description="Amount refunded if applicable",
        example=42.99
    )
    failure_reason: Optional[str] = Field(
        None,
        max_length=500,
        description="Reason for payment failure if applicable",
        example="Insufficient funds"
    )
    payment_details: dict = Field(
        default_factory=dict,
        description="Additional payment details from gateway",
        example={
            "card_last4": "4242",
            "card_brand": "visa",
            "payment_intent": "pi_123456789",
            "receipt_url": "https://example.com/receipts/123"
        }
    )

    model_config = ConfigDict(from_attributes=True)
