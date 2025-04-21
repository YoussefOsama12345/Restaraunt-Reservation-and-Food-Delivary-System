"""
Defines the SQLAlchemy ORM model for Payment entities.

Tracks all payment-related transactions made by users for their orders. This model 
captures essential billing information including status, gateway metadata, transaction 
IDs, timestamps, refund handling, and error reporting.

Classes:
    - PaymentStatusEnum: Enum for payment state transitions
    - Payment: SQLAlchemy model representing a user's payment transaction

Usage:
    The Payment model is used in processing orders, integrating with payment gateways,
    handling refunds, and generating financial reports.
"""

from datetime import datetime
from sqlalchemy import (
    Column, Integer, Float, String, Text, DateTime, ForeignKey, Enum as SqlEnum
)
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from .base import Base


class PaymentStatusEnum(str, PyEnum):
    """
    Enum representing the current status of a payment transaction.
    """
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class Payment(Base):
    """
    Payment model representing a transaction made by a user for an order.

    Attributes:
        - id: Primary key
        - user_id: FK to the User who made the payment
        - order_id: FK to the related Order
        - amount: Total amount paid
        - payment_method: Payment medium used (e.g., credit_card, cash)
        - transaction_id: Identifier returned by the payment gateway
        - status: Current status of the payment
        - payment_gateway: Name of the payment provider
        - payment_details: Optional JSON metadata (e.g., card type, gateway response)
        - completed_at: Timestamp when payment was successfully completed
        - refunded_at: Timestamp when refund was issued (if applicable)
        - refund_amount: Total amount refunded
        - failure_reason: Description of why the payment failed (if any)
        - created_at: Timestamp when payment record was created
        - updated_at: Timestamp for last update

    Relationships:
        - user: Link to the paying User
        - order: Link to the related Order
    """
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50), nullable=False)  # e.g., credit_card, cash
    transaction_id = Column(String(100), nullable=True)
    status = Column(SqlEnum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    payment_gateway = Column(String(50), nullable=True)
    payment_details = Column(Text, nullable=True)  # Store JSON as string
    completed_at = Column(DateTime, nullable=True)
    refunded_at = Column(DateTime, nullable=True)
    refund_amount = Column(Float, nullable=True)
    failure_reason = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="payments")
    order = relationship("Order", back_populates="payment")
