"""
Order management API routes.

Handles placing new orders, retrieving order details, listing orders,
updating order status, cancellation, and tracking delivery information.
All endpoints require user authentication.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order import OrderCreate, OrderRead, OrderUpdateStatus
from app.api.deps import get_current_user, get_db
from app.controllers import order_controller

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderRead)
async def create_order(
    order_data: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Create a new order for the authenticated user.
    Role: User
    """
    try:
        return await order_controller.create_order_controller(order_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve a specific order by its ID.
    Role: User
    """
    try:
        return await order_controller.get_order_controller(order_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=List[OrderRead])
async def list_orders(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List all orders placed by the current user.
    Role: User
    """
    return await order_controller.list_orders_controller(db, current_user)


@router.put("/{order_id}/status", response_model=OrderRead)
async def update_order_status(
    order_id: int,
    status_data: OrderUpdateStatus,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update the status of an existing order (e.g., to 'delivered').
    Role: User
    """
    try:
        return await order_controller.update_order_status_controller(order_id, status_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{order_id}/cancel", response_model=dict)
async def cancel_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Cancel a specific order if it's still eligible for cancellation.
    Role: User
    """
    try:
        return await order_controller.cancel_order_controller(order_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{order_id}/track", response_model=dict)
async def track_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Track the delivery status of an order.
    Role: User
    """
    try:
        return await order_controller.track_order_controller(order_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
