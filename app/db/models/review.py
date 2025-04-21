"""
Defines the SQLAlchemy ORM model for customer reviews.

This model stores user feedback related to restaurants, menu items, and orders. 
Reviews can include a star rating, optional comments, and metadata such as 
verification status and helpful vote counts.

Classes:
    - Review: SQLAlchemy model representing user-generated reviews.

Usage:
    Used in user profiles, restaurant detail pages, menu item ratings, and 
    administrative moderation or analytics dashboards.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Review(Base):
    """
    Review model representing a user's rating and comment on a restaurant, order, or menu item.

    Attributes:
        - id: Primary key
        - user_id: FK to the reviewing user
        - restaurant_id: FK to the reviewed restaurant
        - order_id: (optional) FK to the order this review is based on
        - menu_item_id: (optional) FK to a specific menu item being reviewed
        - rating: Integer score (typically 1-5 stars)
        - comment: Optional text feedback
        - menu_item_name: Snapshot of menu item name (denormalized)
        - restaurant_name: Snapshot of restaurant name (denormalized)
        - user_name: Snapshot of user's display name (denormalized)
        - is_verified: Boolean indicating if the review is from a verified order
        - helpful_votes: Count of users who found this review helpful
        - created_at: Timestamp of review creation
        - updated_at: Timestamp of last update

    Relationships:
        - user: Reviewer (User)
        - restaurant: Reviewed Restaurant
        - order: Associated Order (if any)
        - menu_item: Reviewed MenuItem (if any)
    """
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    rating = Column(Integer, nullable=False)  # 1-5 stars
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    menu_item_name = Column(String(100), nullable=True)
    restaurant_name = Column(String(100), nullable=True)
    user_name = Column(String(100), nullable=True)
    is_verified = Column(Boolean, default=False)
    helpful_votes = Column(Integer, default=0)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")
    order = relationship("Order")
    menu_item = relationship("MenuItem", back_populates="reviews")
