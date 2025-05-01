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
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.db.models.reservation import Reservation
from datetime import datetime


# Role : User


# Placeholder models/schemas for standalone usage
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


async def create_reservation(reservation_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Create a new table reservation.

    Role: User
    """
    # Map 'reservation_time' from reservation_data to 'reservation_date' for DB
    if 'reservation_time' in reservation_data:
        reservation_data['reservation_date'] = reservation_data.pop('reservation_time')
    reservation_fields = {k: v for k, v in reservation_data.items() if k in Reservation.__table__.columns.keys()}
    reservation_fields['user_id'] = user_id
    reservation_fields['created_at'] = datetime.utcnow()
    reservation_fields['updated_at'] = datetime.utcnow()
    reservation = Reservation(**reservation_fields)
    db.add(reservation)
    await db.commit()
    await db.refresh(reservation)
    # Map reservation_date from DB to reservation_time for API response compatibility
    result_dict = {c.name: getattr(reservation, c.name) for c in Reservation.__table__.columns}
    if 'reservation_date' in result_dict:
        result_dict['reservation_time'] = result_dict['reservation_date']
    return result_dict


async def get_reservation(reservation_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve a specific reservation by ID.

    Role: User
    """
    result = await db.execute(select(Reservation).where(Reservation.id == reservation_id, Reservation.user_id == user_id))
    reservation = result.scalars().first()
    if not reservation:
        raise Exception("Reservation not found or unauthorized")
    result_dict = {c.name: getattr(reservation, c.name) for c in Reservation.__table__.columns}
    if 'reservation_date' in result_dict:
        result_dict['reservation_time'] = result_dict['reservation_date']
    return result_dict


async def list_reservations(user_id: int, db: AsyncSession) -> list:
    """
    List reservations, optionally filtered by user.

    Role: User
    """
    result = await db.execute(select(Reservation).where(Reservation.user_id == user_id))
    reservations = result.scalars().all()
    output = []
    for r in reservations:
        r_dict = {c.name: getattr(r, c.name) for c in Reservation.__table__.columns}
        if 'reservation_date' in r_dict:
            r_dict['reservation_time'] = r_dict['reservation_date']
        output.append(r_dict)
    return output


async def update_reservation(reservation_id: int, reservation_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Update an existing reservation's data.

    Role: User
    """
    result = await db.execute(select(Reservation).where(Reservation.id == reservation_id, Reservation.user_id == user_id))
    reservation = result.scalars().first()
    if not reservation:
        raise Exception("Reservation not found or unauthorized")
    for field, value in reservation_data.items():
        if field in Reservation.__table__.columns.keys() and value is not None and field != "user_id":
            setattr(reservation, field, value)
    reservation.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(reservation)
    # Map reservation_date to reservation_time for API response compatibility
    result_dict = {c.name: getattr(reservation, c.name) for c in Reservation.__table__.columns}
    if 'reservation_date' in result_dict:
        result_dict['reservation_time'] = result_dict['reservation_date']
    return result_dict


async def cancel_reservation(reservation_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Cancel a reservation by marking it as 'cancelled'.

    Role: User
    """
    result = await db.execute(select(Reservation).where(Reservation.id == reservation_id, Reservation.user_id == user_id))
    reservation = result.scalars().first()
    if not reservation:
        raise Exception("Reservation not found or unauthorized")
    reservation.status = "cancelled"
    reservation.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(reservation)
    return {"detail": "Reservation cancelled", "id": reservation.id}
