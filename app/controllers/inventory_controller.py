"""
Inventory Controller

Handles inventory operations for ingredients and stock management.
Delegates core business logic to the inventory_service module.
Only accessible by admin users.
"""

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.services.inventory_service import (
    create_inventory_item as svc_create_inventory_item,
    get_inventory_item as svc_get_inventory_item,
    list_inventory_items as svc_list_inventory_items,
    update_inventory_item as svc_update_inventory_item,
    delete_inventory_item as svc_delete_inventory_item,
    list_low_stock_items as svc_list_low_stock_items,
)
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate, InventoryItemRead

# Dummy admin check (replace with your actual RBAC logic)
def require_admin(current_user):
    if not (getattr(current_user, "is_admin", False) or getattr(current_user, "role", None) == "admin"):
        raise HTTPException(status_code=403, detail="Admin privileges required.")

async def create_inventory_item(
    item_data: InventoryItemCreate,
    db: AsyncSession,
    current_user
):
    """
    Add a new inventory item (e.g., ingredient or supply).
    Role: Admin
    """
    require_admin(current_user)
    try:
        restaurant_id = item_data.restaurant_id
        result = await svc_create_inventory_item(db, item_data, restaurant_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def list_inventory_items(
    db: AsyncSession,
    current_user
):
    """
    Retrieve a list of all inventory items.
    Role: Admin
    """
    require_admin(current_user)
    restaurant_id = getattr(current_user, "restaurant_id", 1)
    return await svc_list_inventory_items(db, restaurant_id)

async def get_inventory_item(
    item_id: int,
    db: AsyncSession,
    current_user
):
    """
    Retrieve a specific inventory item by ID.
    Role: Admin
    """
    require_admin(current_user)
    return await svc_get_inventory_item(db, item_id)

async def update_inventory_item(
    item_id: int,
    item_data: InventoryItemUpdate,
    db: AsyncSession,
    current_user
):
    """
    Update details (e.g., quantity, threshold) of an inventory item.
    Role: Admin
    """
    require_admin(current_user)
    try:
        return await svc_update_inventory_item(db, item_id, item_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def delete_inventory_item(
    item_id: int,
    db: AsyncSession,
    current_user
):
    """
    Remove an inventory item from the system.
    Role: Admin
    """
    require_admin(current_user)
    try:
        return await svc_delete_inventory_item(db, item_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def list_low_stock_items(
    threshold: int,
    db: AsyncSession,
    current_user
):
    """
    List inventory items below the defined stock threshold.
    Role: Admin
    """
    require_admin(current_user)
    restaurant_id = getattr(current_user, "restaurant_id", 1)
    return await svc_list_low_stock_items(db, restaurant_id, threshold if threshold else None)
