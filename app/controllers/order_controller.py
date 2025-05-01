"""
Order Controller

Handles user requests related to placing and managing food orders.

Delegates business logic to the `order_service` module and enforces
authentication and user-specific access control.

Roles:
- User: Place, view, update, cancel, and track orders
"""

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from app.schemas.order import OrderCreate, OrderRead, OrderUpdateStatus
from app.services import order_service

async def create_order_controller(
    order_data: OrderCreate,
    db: AsyncSession,
    current_user
) -> OrderRead:
    """
    Create a new food order.
    Role: User
    """
    try:
        order_dict = order_data.dict()
        order = await order_service.create_order(order_dict, current_user.id, db)
        return OrderRead(**order)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def get_order_controller(
    order_id: int,
    db: AsyncSession,
    current_user
) -> OrderRead:
    """
    Get details of a specific order.
    Role: User
    """
    try:
        order = await order_service.get_order(order_id, current_user.id, db)
        return OrderRead(**order)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

async def list_orders_controller(
    db: AsyncSession,
    current_user
) -> List[OrderRead]:
    """
    List all orders of the current user.
    Role: User
    """
    orders = await order_service.list_orders(current_user.id, db)
    return [OrderRead(**order) for order in orders]

async def update_order_status_controller(
    order_id: int,
    status_data: OrderUpdateStatus,
    db: AsyncSession,
    current_user
) -> OrderRead:
    """
    Update the status of a specific order.
    Role: User
    """
    try:
        status_dict = status_data.dict(exclude_unset=True)
        order = await order_service.update_order_status(order_id, status_dict, current_user.id, db)
        return OrderRead(**order)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def cancel_order_controller(
    order_id: int,
    db: AsyncSession,
    current_user
) -> dict:
    """
    Cancel a specific order.
    Role: User
    """
    try:
        result = await order_service.cancel_order(order_id, current_user.id, db)
        return jsonable_encoder(result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def track_order_controller(
    order_id: int,
    db: AsyncSession,
    current_user
) -> dict:
    """
    Track the current status and delivery progress of an order.
    Role: User
    """
    try:
        result = await order_service.track_order(order_id, current_user.id, db)
        return jsonable_encoder(result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
