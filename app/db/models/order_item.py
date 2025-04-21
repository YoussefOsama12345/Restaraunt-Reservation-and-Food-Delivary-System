"""
Defines the SQLAlchemy ORM model for OrderItem entities.

Each `OrderItem` represents an individual menu item included in a specific order.
It stores quantity, pricing at the time of order, and optional custom instructions,
allowing historical accuracy and item-level tracking.

Classes:
    - OrderItem: SQLAlchemy model representing an item within an order.

Usage:
    This model is used to track detailed contents of each order for reporting,
    billing, and order fulfillment processes.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class OrderItem(Base):
    """
    OrderItem model representing a single menu item in a customer's order.

    Attributes:
        - id: Primary key
        - order_id: Foreign key linking to the parent order
        - menu_item_id: Foreign key linking to the ordered menu item
        - quantity: Number of units ordered
        - price_at_time: Snapshot of item price at the time of order
        - special_instructions: Optional instructions for this item (e.g., "extra cheese")
        - created_at: Timestamp when the item was added to the order

    Relationships:
        - order: Parent Order object this item belongs to
        - menu_item: Reference to the MenuItem that was ordered
    """
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)
    special_instructions = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    order = relationship("Order", back_populates="order_items")
    menu_item = relationship("MenuItem", back_populates="order_items")
