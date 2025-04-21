"""
models/menu_item.py

Defines the SQLAlchemy ORM model for menu items offered by restaurants.

Each `MenuItem` instance represents a dish or drink listed on a restaurant's menu.
This model stores pricing, availability, dietary details, nutritional information,
and relationships to categories, restaurants, and user interactions like cart items,
orders, and reviews.

Classes:
    - MenuItem: SQLAlchemy model representing a menu item with full metadata.

Usage:
    This model is used to populate restaurant menus, manage item availability,
    track order and review statistics, and support filtering by category or tag.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class MenuItem(Base):
    """
    MenuItem model representing a single item on a restaurant's menu.

    Attributes:
        - id: Primary key
        - name: Unique name of the menu item
        - description: Optional description text
        - price: Price of the item
        - image_url: Optional image link
        - available: Availability flag
        - is_vegetarian: Dietary flag
        - category_id: FK to the item's category (nullable, SET NULL on delete)
        - restaurant_id: FK to the restaurant that owns this item
        - created_at: Timestamp when item was created
        - updated_at: Timestamp for last update
        - preparation_time: Estimated preparation time in minutes
        - calories: Nutritional calorie value
        - ingredients: Text list of ingredients
        - total_orders: Count of how many times ordered
        - average_rating: Average customer rating
        - last_ordered_at: Timestamp of the last time this item was ordered
        - nutritional_info: Additional nutritional data
        - cooking_instructions: Optional cooking/prep notes
        - serving_size: Portion/size info
        - tags: Comma-separated keywords for filtering/search

    Relationships:
        - category: Many-to-one relationship with Category
        - restaurant: Many-to-one relationship with Restaurant
        - cart_items: One-to-many relationship with CartItem
        - order_items: One-to-many relationship with OrderItem
        - reviews: One-to-many relationship with Review
    """
    __tablename__ = "menu_items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    image_url = Column(String(255), nullable=True)
    available = Column(Boolean, default=True)
    is_vegetarian = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    preparation_time = Column(Integer, nullable=True)
    calories = Column(Integer, nullable=True)
    ingredients = Column(Text, nullable=True)
    total_orders = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    last_ordered_at = Column(DateTime, nullable=True)
    nutritional_info = Column(Text, nullable=True)
    cooking_instructions = Column(Text, nullable=True)
    serving_size = Column(String(100), nullable=True)
    tags = Column(String(500), nullable=True)
    
    # Relationships
    category = relationship("Category", back_populates="menu_items")
    restaurant = relationship("Restaurant", back_populates="menu_items")
    cart_items = relationship("CartItem", back_populates="menu_item")
    order_items = relationship("OrderItem", back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item")
