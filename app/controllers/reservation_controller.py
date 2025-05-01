"""
Reservation Controller

Handles reservation-related user requests and delegates business logic
to the reservation_service module.

Roles:
- User: Can create, update, cancel, and view reservations
"""

from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import reservation_service
from app.schemas.reservation import ReservationCreate, ReservationUpdate, ReservationRead


async def create_reservation_controller(
    reservation_data: ReservationCreate,
    user_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends(),
) -> ReservationRead:
    """
    Create a new table reservation.
    Role: User
    """
    try:
        reservation_dict = reservation_data.dict()
        result = await reservation_service.create_reservation(reservation_dict, user_id, db)
        return ReservationRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_reservation_controller(
    reservation_id: int,
    user_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends(),
) -> ReservationRead:
    """
    Get a reservation by its ID.
    Role: User
    """
    try:
        result = await reservation_service.get_reservation(reservation_id, user_id, db)
        return ReservationRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def list_reservations_controller(
    user_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends(),
) -> List[ReservationRead]:
    """
    List reservations. Optionally filter by user ID.
    Role: User
    """
    try:
        results = await reservation_service.list_reservations(user_id, db)
        return [ReservationRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def update_reservation_controller(
    reservation_id: int,
    reservation_data: ReservationUpdate,
    user_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends(),
) -> ReservationRead:
    """
    Update an existing reservation.
    Role: User
    """
    try:
        update_dict = reservation_data.dict(exclude_unset=True)
        result = await reservation_service.update_reservation(reservation_id, update_dict, user_id, db)
        return ReservationRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def cancel_reservation_controller(
    reservation_id: int,
    user_id: int,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends(),
) -> dict:
    """
    Cancel an existing reservation.
    Role: User
    """
    try:
        return await reservation_service.cancel_reservation(reservation_id, user_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
