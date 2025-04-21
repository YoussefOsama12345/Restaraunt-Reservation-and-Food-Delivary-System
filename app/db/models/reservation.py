"""
models/reservation.py

Defines the SQLAlchemy ORM model for handling restaurant reservations made by users.

Each Reservation record stores essential data for managing bookings, including
user identity, restaurant location, party size, reservation date, and any
special notes.

Classes:
    - Reservation: SQLAlchemy model representing a user's restaurant reservation.

Usage:
    Used in features related to table bookings, scheduling, availability management,
    user reservation history, and restaurant-side confirmations.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Reservation(Base):
    """
    Reservation model representing a user's table booking at a restaurant.

    Attributes:
        - id: Primary key
        - user_id: FK to the user who made the reservation
        - restaurant_id: FK to the restaurant where the reservation is made
        - reservation_date: Scheduled datetime for the reservation
        - party_size: Number of people in the reservation
        - status: Current state of the reservation (pending, confirmed, etc.)
        - special_requests: Optional text for notes or accessibility requests
        - created_at: Timestamp when the reservation was created
        - updated_at: Timestamp for last modification

    Relationships:
        - user: Link to the User who made the reservation
        - restaurant: Link to the Restaurant where the reservation is held
    """
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    reservation_date = Column(DateTime, nullable=False)
    party_size = Column(Integer, nullable=False)
    status = Column(String(20), default="pending")  # pending, confirmed, cancelled, completed
    special_requests = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="reservations")
    restaurant = relationship("Restaurant", back_populates="reservations")
