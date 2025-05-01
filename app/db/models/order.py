"""
models/order.py

Defines the SQLAlchemy ORM model for orders placed by users.

The Order model represents the transactional data of a user's food order,
including references to user details, delivery address, restaurant, payment,
and delivery personnel. It supports status tracking, delivery times, and
special instructions.

Classes:
    - Order: SQLAlchemy model representing a customer's order.

Usage:
    This model is used to store and manage order lifecycle data such as
    creation, payment, delivery status, and assignment to drivers. It is
    central to order processing, reporting, and customer service workflows.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .base import Base


class Order(Base):
    """
    Order model representing a food order made by a user.

    Attributes:
        - id: Primary key
        - user_id: FK to the user who placed the order
        - delivery_address_id: FK to the address where the order is delivered
        - status: Current status of the order (e.g., pending, delivered)
        - total_amount: Final price after all calculations
        - payment_status: Tracks whether payment is pending, paid, or failed
        - special_instructions: Optional text field for additional delivery or prep notes
        - created_at: Timestamp when the order was created
        - updated_at: Timestamp for last update
        - restaurant_id: FK to the restaurant fulfilling the order
        - order_number: Unique alphanumeric order reference
        - estimated_delivery_time: Expected delivery timestamp
        - actual_delivery_time: Actual delivery timestamp (if delivered)
        - delivery_person_id: FK to the assigned delivery user (nullable)

    Relationships:
        - user: Link to the User who placed the order
        - delivery_address: Address where the order should be delivered
        - order_items: List of individual items included in the order
        - payment: One-to-one relationship with Payment
        - delivery_task: Task record for delivery personnel
        - restaurant: Link to the Restaurant fulfilling the order
        - delivery_person: User assigned to deliver the order
        - reviews: List of reviews left for this order
    """
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    delivery_address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    status = Column(String(20), default="pending")  # pending, confirmed, preparing, out_for_delivery, delivered, cancelled
    total_amount = Column(Float, nullable=False)
    payment_status = Column(String(20), default="pending")  # pending, paid, failed, refunded
    special_instructions = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    order_number = Column(String(50), unique=True, nullable=False)
    estimated_delivery_time = Column(DateTime, nullable=True)
    actual_delivery_time = Column(DateTime, nullable=True)
    delivery_person_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="orders", foreign_keys=[user_id])
    delivery_address = relationship("Address", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    payment = relationship("Payment", back_populates="order", uselist=False)
    delivery_task = relationship("DeliveryTask", back_populates="order", uselist=False)
    restaurant = relationship("Restaurant", back_populates="orders")
    delivery_person = relationship("User", foreign_keys=[delivery_person_id], overlaps="assigned_deliveries")
    reviews = relationship("Review", back_populates="order")
