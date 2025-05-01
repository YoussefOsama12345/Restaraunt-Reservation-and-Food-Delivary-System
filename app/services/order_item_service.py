"""
Order Item Service

Handles logic for managing items within a specific order, including:
- Adding new items
- Retrieving individual order items
- Listing all items in an order
- Updating order item details
- Deleting order items

Role: User
"""

from typing import List, Optional, Dict
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.order_item import OrderItem
from app.db.models.order import Order
from app.utils.db_helpers import handle_missing_greenlet
from app.db.models.menu_item import MenuItem


@handle_missing_greenlet
async def add_order_item(db: AsyncSession, order_id: int, item_data: dict, user_id: int) -> dict:
    """
    Add a new item to an existing order.
    Role: User
    """
    # Check if order exists and belongs to the user
    result = await db.execute(select(Order).where(Order.id == order_id, Order.user_id == user_id))
    order = result.scalars().first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or unauthorized")
    
    # Check if menu item exists
    menu_item_id = item_data.get("menu_item_id")
    result = await db.execute(select(MenuItem).where(MenuItem.id == menu_item_id))
    menu_item = result.scalars().first()
    if not menu_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    
    # Prepare order item fields
    valid_keys = OrderItem.__table__.columns.keys()
    data_filtered = {k: v for k, v in item_data.items() if k in valid_keys}
    data_filtered["order_id"] = order_id
    data_filtered["price_at_time"] = menu_item.price  # snapshot price
    
    # Create and save the order item
    order_item = OrderItem(**data_filtered)
    db.add(order_item)
    await db.commit()
    await db.refresh(order_item)
    
    return {k: getattr(order_item, k) for k in valid_keys}


@handle_missing_greenlet
async def get_order_item(db: AsyncSession, item_id: int, user_id: int) -> dict:
    """
    Retrieve a specific order item by ID.
    Role: User
    """
    # First get the order item
    item_result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    order_item = item_result.scalars().first()
    
    if not order_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")
    
    # Then verify the order belongs to the user
    order_result = await db.execute(select(Order).where(Order.id == order_item.order_id, Order.user_id == user_id))
    order = order_result.scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this order item")
    
    # Return the order item as a dictionary
    return {k: getattr(order_item, k) for k in OrderItem.__table__.columns.keys()}


@handle_missing_greenlet
async def list_order_items(db: AsyncSession, order_id: int, user_id: int) -> List[dict]:
    """
    List all items in a specific order.
    Role: User
    """
    # First verify the order exists and belongs to the user
    order_result = await db.execute(
        select(Order).where(Order.id == order_id, Order.user_id == user_id)
    )
    order = order_result.scalars().first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or unauthorized")
    
    # Then get the order items directly without joining
    items_result = await db.execute(
        select(OrderItem).where(OrderItem.order_id == order_id)
    )
    items = items_result.scalars().all()
    
    # Convert to dictionary format
    return [{k: getattr(item, k) for k in OrderItem.__table__.columns.keys()} for item in items]


# This function is now redundant with the @handle_missing_greenlet decorator
# But kept for backward compatibility
def list_order_items_sync(order_id: int, user_id: int) -> List[dict]:
    """
    Synchronous version of list_order_items.
    This is a fallback for when the async version encounters greenlet issues.
    
    Role: User
    """
    from app.services.order_item_service_sync import list_order_items_sync as sync_impl
    return sync_impl(order_id, user_id)


@handle_missing_greenlet
async def update_order_item(db: AsyncSession, item_id: int, update_data: dict, user_id: int) -> dict:
    """
    Update an existing order item's details.
    Role: User
    """
    # First get the order item
    item_result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    order_item = item_result.scalars().first()
    
    if not order_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")
    
    # Then verify the order belongs to the user
    order_result = await db.execute(select(Order).where(Order.id == order_item.order_id, Order.user_id == user_id))
    order = order_result.scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this order item")
    
    # Update the fields
    for field, value in update_data.items():
        if value is not None and hasattr(order_item, field):
            setattr(order_item, field, value)
    
    await db.commit()
    await db.refresh(order_item)
    
    # Return the updated order item as a dictionary
    return {k: getattr(order_item, k) for k in OrderItem.__table__.columns.keys()}


@handle_missing_greenlet
async def delete_order_item(db: AsyncSession, item_id: int, user_id: int) -> dict:
    """
    Delete an item from an order.
    Role: User
    """
    # First get the order item
    item_result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    order_item = item_result.scalars().first()
    
    if not order_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")
    
    # Then verify the order belongs to the user
    order_result = await db.execute(select(Order).where(Order.id == order_item.order_id, Order.user_id == user_id))
    order = order_result.scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this order item")
    
    # Delete the order item
    await db.delete(order_item)
    await db.commit()
    
    return {"detail": "Order item deleted successfully"}
