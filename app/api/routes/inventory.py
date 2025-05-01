"""
Inventory management API routes.

This module defines FastAPI routes for managing inventory items such as ingredients,
supplies, and packaging materials used in the restaurant system. It supports:
- Creating inventory items
- Retrieving individual or all inventory records
- Updating existing items
- Deleting inventory records
- Listing low-stock alerts

Access Control:
All endpoints are restricted to users with admin privileges.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate, InventoryItemRead
from app.api.deps import get_current_user, get_db
from app.controllers import inventory_controller

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.post("/", response_model=InventoryItemRead)
async def create_inventory_item(
    item_data: InventoryItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Create a new inventory item. Admin only.
    """
    try:
        return await inventory_controller.create_inventory_item(item_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[InventoryItemRead])
async def list_inventory_items(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve all inventory items. Admin only.
    """
    return await inventory_controller.list_inventory_items(db, current_user)

@router.get("/{item_id}", response_model=InventoryItemRead)
async def get_inventory_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve a specific inventory item by ID. Admin only.
    """
    return await inventory_controller.get_inventory_item(item_id, db, current_user)

@router.put("/{item_id}", response_model=InventoryItemRead)
async def update_inventory_item(
    item_id: int,
    item_data: InventoryItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update an inventory item. Admin only.
    """
    try:
        return await inventory_controller.update_inventory_item(item_id, item_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{item_id}", response_model=dict)
async def delete_inventory_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete an inventory item. Admin only.
    """
    try:
        return await inventory_controller.delete_inventory_item(item_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/low-stock/", response_model=List[InventoryItemRead])
async def list_low_stock_items(
    threshold: int = 0,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List low-stock inventory items. Admin only.
    """
    return await inventory_controller.list_low_stock_items(threshold, db, current_user)
