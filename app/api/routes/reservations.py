"""
Reservation booking API routes.

Manages table reservations with support for creating, retrieving, listing,
updating, and canceling reservations, including guest count and special requests.
All endpoints require user authentication.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reservation import ReservationCreate, ReservationUpdate, ReservationRead
from app.api.deps import get_current_user, get_db
from app.controllers import reservation_controller

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.post("/", response_model=ReservationRead)
async def create_reservation(
    reservation_data: ReservationCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Create a new table reservation.
    Role: User
    """
    try:
        return await reservation_controller.create_reservation_controller(reservation_data, current_user.id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{reservation_id}", response_model=ReservationRead)
async def get_reservation(
    reservation_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve detailed information for a specific reservation by ID.
    Role: User
    """
    try:
        return await reservation_controller.get_reservation_controller(reservation_id, current_user.id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=List[ReservationRead])
async def list_reservations(
    user_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List reservations, optionally filtered by user ID.
    Role: User
    """
    try:
        uid = user_id if user_id is not None else current_user.id
        return await reservation_controller.list_reservations_controller(uid, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{reservation_id}", response_model=ReservationRead)
async def update_reservation(
    reservation_id: int,
    reservation_data: ReservationUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update an existing reservation by ID.
    Role: User
    """
    try:
        return await reservation_controller.update_reservation_controller(reservation_id, reservation_data, current_user.id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{reservation_id}", response_model=dict)
async def cancel_reservation(
    reservation_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Cancel an existing reservation by ID.
    Role: User
    """
    try:
        return await reservation_controller.cancel_reservation_controller(reservation_id, current_user.id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
