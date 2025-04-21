"""
models/cart_item.py

Defines the SQLAlchemy ORM model for CartItem entities representing items added to a user's cart.

Each CartItem links a user with a specific menu item, including quantity and optional details
like special instructions or selected add-ons. This model is a key component of the order-building
process in a restaurant or food delivery application.

Classes:
    - CartItem: SQLAlchemy model representing a user's selected menu item in the shopping cart.

Usage:
    Used to track user's in-progress orders before checkout. Supports customization
    like special instructions or option selections.
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class CartItem(Base):
    """
    CartItem model representing a selected menu item in a user's cart.

    Attributes:
        - id: Primary key
        - user_id: Foreign key linking to the user who added the item
        - menu_item_id: Foreign key linking to the selected menu item
        - quantity: Number of units selected
        - created_at: Timestamp when item was added to the cart
        - updated_at: Timestamp for last modification
        - special_instructions: Optional text notes (e.g., "no onions")
        - selected_options: Optional JSON string storing selected extras, sizes, etc.

    Relationships:
        - user: Many-to-one relationship to the User who owns the cart
        - menu_item: Many-to-one relationship to the MenuItem being added
    """
    __tablename__ = "cart_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    special_instructions = Column(Text, nullable=True)
    selected_options = Column(Text, nullable=True)  # Store as JSON string
    
    # Relationships
    user = relationship("User", back_populates="cart_items")
    menu_item = relationship("MenuItem", back_populates="cart_items")
