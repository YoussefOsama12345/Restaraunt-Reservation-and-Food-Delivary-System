"""
models/restaurant.py

Defines the SQLAlchemy ORM model for Restaurant entities in the system.

This model represents restaurants registered on the platform, storing metadata such as 
location, contact details, operational status, cuisine types, and configurations for 
delivery and capacity. It also connects the restaurant to various entities like 
menu items, reservations, reviews, orders, and delivery tasks.

Classes:
    - Restaurant: SQLAlchemy model representing a restaurant and its properties.

Usage:
    Used to manage restaurant data, associate menu and inventory items,
    track reviews and reservations, and link with delivery logistics.
"""

from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Restaurant(Base):
    """
    Restaurant model representing a dining or delivery venue on the platform.

    Attributes:
        - id: Primary key
        - name: Unique restaurant name
        - description: Optional detailed description of the restaurant
        - location: Physical address or coordinates
        - cuisine_type: Category of cuisine (e.g., Italian, Chinese)
        - phone: Optional contact number
        - is_active: Boolean flag to indicate if the restaurant is operational
        - created_at: Timestamp when the restaurant was added
        - updated_at: Timestamp of the last update
        - opening_hours: Textual representation of open times
        - website: Link to official website or profile
        - capacity: Number of people the restaurant can serve
        - delivery_radius: Radius (in km) for delivery availability
        - minimum_order: Minimum order amount for delivery
        - average_rating: Average customer rating
        - total_reviews: Count of all submitted reviews

    Relationships:
        - menu_items: One-to-many relationship with MenuItem
        - reservations: One-to-many relationship with Reservation
        - reviews: One-to-many relationship with Review
        - orders: One-to-many relationship with Order
        - delivery_tasks: One-to-many with DeliveryTask
    """
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=False)
    cuisine_type = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    opening_hours = Column(String(200), nullable=True)
    website = Column(String(255), nullable=True)
    capacity = Column(Integer, nullable=True)
    delivery_radius = Column(Float, nullable=True)
    minimum_order = Column(Float, nullable=True)
    average_rating = Column(Float, nullable=True)
    total_reviews = Column(Integer, default=0)
    
    # Relationships
    menu_items = relationship("MenuItem", back_populates="restaurant")
    reservations = relationship("Reservation", back_populates="restaurant")
    reviews = relationship("Review", back_populates="restaurant")
    # inventory_items = relationship("InventoryItem", back_populates="restaurant", cascade="all, delete-orphan")  # DISABLED: No such model exists
    orders = relationship("Order", back_populates="restaurant")
    # delivery_tasks = relationship("DeliveryTask", back_populates="restaurant")  # DISABLED: No property 'restaurant' on DeliveryTask
