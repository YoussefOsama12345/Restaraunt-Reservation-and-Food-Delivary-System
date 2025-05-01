"""
Order Item Controller

Handles API-level logic for managing individual items within an order.

Delegates business logic to the `order_item_service` module and ensures
user-specific access for viewing and manipulating order contents.

Roles:
- User: View, add, update, or remove items from their order
"""

from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from app.services import order_item_service
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate, OrderItemRead

async def add_order_item_controller(
    order_id: int,
    item_data: OrderItemCreate,
    db: AsyncSession,
    current_user
) -> OrderItemRead:
    """
    Add a new item to an existing order.
    Role: User
    """
    try:
        item_dict = item_data.dict()
        order_item = await order_item_service.add_order_item(db, order_id, item_dict, current_user.id)
        return OrderItemRead(**order_item)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def get_order_item_controller(
    item_id: int,
    db: AsyncSession,
    current_user
) -> OrderItemRead:
    """
    Retrieve details of a specific order item.
    Role: User
    """
    try:
        order_item = await order_item_service.get_order_item(db, item_id, current_user.id)
        return OrderItemRead(**order_item)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

async def list_order_items_controller(
    order_id: int,
    db: AsyncSession,
    current_user
) -> List[OrderItemRead]:
    """
    List all items in a specific order.
    Role: User
    """
    try:
        try:
            # Try the async version first
            items = await order_item_service.list_order_items(db, order_id, current_user.id)
        except Exception as async_error:
            # Check if it's a MissingGreenlet error
            error_str = str(async_error)
            if "MissingGreenlet" in error_str or "greenlet_spawn has not been called" in error_str:
                print(f"Warning: Falling back to sync implementation due to: {error_str}")
                # Use the synchronous version directly
                from app.services.order_item_service_sync import list_order_items_sync
                items = list_order_items_sync(order_id, current_user.id)
            else:
                # If it's not a MissingGreenlet error, re-raise
                raise async_error
                
        return [OrderItemRead(**item) for item in items]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def update_order_item_controller(
    item_id: int,
    update_data: OrderItemUpdate,
    db: AsyncSession,
    current_user
) -> OrderItemRead:
    """
    Update quantity or instructions of an order item.
    Role: User
    """
    try:
        update_dict = update_data.dict(exclude_unset=True)
        order_item = await order_item_service.update_order_item(db, item_id, update_dict, current_user.id)
        return OrderItemRead(**order_item)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def delete_order_item_controller(
    item_id: int,
    db: AsyncSession,
    current_user
) -> dict:
    """
    Remove an item from an order.
    Role: User
    """
    try:
        result = await order_item_service.delete_order_item(db, item_id, current_user.id)
        return jsonable_encoder(result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
