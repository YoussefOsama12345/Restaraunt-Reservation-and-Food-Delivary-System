"""
Order item API routes.

Handles adding, retrieving, updating, and deleting individual items 
within a food order. All endpoints require user authentication.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user, get_db
from app.controllers import order_item_controller
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate, OrderItemRead

router = APIRouter(prefix="/order-items", tags=["order-items"])


@router.post("/{order_id}", response_model=OrderItemRead)
async def add_order_item(
    order_id: int,
    item_data: OrderItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Add a new item to an existing order.
    Role: User
    """
    try:
        return await order_item_controller.add_order_item_controller(order_id, item_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{item_id}", response_model=OrderItemRead)
async def get_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve a specific item from an order.
    Role: User
    """
    try:
        return await order_item_controller.get_order_item_controller(item_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/order/{order_id}", response_model=List[OrderItemRead])
async def list_order_items(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List all items for a specific order.
    Role: User
    """
    try:
        return await order_item_controller.list_order_items_controller(order_id, db, current_user)
    except Exception as e:
        error_str = str(e)
        if "MissingGreenlet" in error_str or "greenlet_spawn has not been called" in error_str:
            # Handle MissingGreenlet errors directly at the route level
            from app.services.order_item_service_sync import list_order_items_sync
            items = list_order_items_sync(order_id, current_user.id)
            return [OrderItemRead(**item) for item in items]
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{item_id}", response_model=OrderItemRead)
async def update_order_item(
    item_id: int,
    update_data: OrderItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update the quantity or special instructions of an item in an order.
    Role: User
    """
    try:
        return await order_item_controller.update_order_item_controller(item_id, update_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{item_id}", response_model=dict)
async def delete_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Remove an item from an order.
    Role: User
    """
    try:
        return await order_item_controller.delete_order_item_controller(item_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
