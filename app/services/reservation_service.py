"""
Reservation Service

Handles table booking operations, including:
- Creating new reservations
- Fetching individual reservation details
- Listing all or user-specific reservations
- Updating reservation details
- Canceling reservations

Role: User
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


# Role : User


# Placeholder models/schemas for standalone usage
class Reservation:
    id: int
    user_id: int
    date: str
    time: str
    guests: int
    special_requests: Optional[str]


class ReservationCreate:
    date: str
    time: str
    guests: int
    special_requests: Optional[str]


class ReservationUpdate:
    date: Optional[str]
    time: Optional[str]
    guests: Optional[int]
    special_requests: Optional[str]


def create_reservation(reservation_data: ReservationCreate, user_id: int) -> Reservation:
    """
    Create a new table reservation.

    Role: User
    """
    pass


def get_reservation(reservation_id: int, user_id: int) -> Reservation:
    """
    Retrieve a specific reservation by ID.

    Role: User
    """
    pass


def list_reservations(user_id: Optional[int] = None) -> List[Reservation]:
    """
    List reservations, optionally filtered by user.

    Role: User
    """
    pass


def update_reservation(reservation_id: int, update_data: ReservationUpdate, user_id: int) -> Reservation:
    """
    Update an existing reservation's data.

    Role: User
    """
    pass


def cancel_reservation(reservation_id: int, user_id: int) -> dict:
    """
    Cancel a reservation by marking it as 'cancelled'.

    Role: User
    """
    pass
