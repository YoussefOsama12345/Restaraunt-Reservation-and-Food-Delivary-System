"""
Reservation Module

This module defines the `Reservation` model for the Restaurant Management System (RMS).
The `Reservation` model stores details about customer reservations, including reservation
date, time, guest count, and the table associated with the reservation.

Models:
-------
- Reservation: Represents a reservation made by a customer for a specific date, time, and table.

Usage:
------
The `Reservation` model is used to manage and track customer reservations in the restaurant,
including the number of guests and the assigned table.
"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class Reservation(Base):
    """
    Reservation model stores information about customer reservations,
    including date, time, guest count, and table association.
    """
    __tablename__ = "reservations"

    def __repr__(self):
        return f"<Reservation(reservation_id={self.reservation_id}, customer_name={self.customer_name})>"