"""
models/address.py

Defines the SQLAlchemy ORM model for storing user addresses.

This model allows each user to have multiple saved addresses for delivery or pickup purposes.
It tracks metadata like default selection, usage frequency, and last use timestamp, and is 
linked to the `User` and `Order` models through relationships.

Classes:
    - Address: SQLAlchemy model representing a user's delivery or billing address.

Usage:
    Addresses are used during order placement, profile management, and delivery dispatching.
    The model supports setting default addresses and tracking how often each is used.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Address(Base):
    """
    Address model representing a physical delivery or billing address associated with a user.

    Attributes:
        - id: Primary key
        - user_id: Foreign key linking to the user
        - street_address: Detailed street and number
        - city: City name
        - state: State or province
        - postal_code: ZIP or postal code
        - country: Country name
        - is_default: Indicates if this is the user's primary address
        - created_at: Timestamp when address was added
        - updated_at: Timestamp for last modification
        - label: Optional short name like 'Home' or 'Work'
        - is_active: If the address is still valid or used
        - last_used_at: When the address was last used
        - usage_count: Number of times this address has been used for orders

    Relationships:
        - user: Many-to-one relationship with the User model
        - orders: One-to-many relationship with orders delivered to this address
    """
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    street_address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    label = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    last_used_at = Column(DateTime, nullable=True)
    usage_count = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="addresses")
    orders = relationship("Order", back_populates="delivery_address")
