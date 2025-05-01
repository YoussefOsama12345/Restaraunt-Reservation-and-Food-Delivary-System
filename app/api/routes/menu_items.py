"""
Service layer for Menu Item operations.

Encapsulates all business logic related to menu items:
- Creating new menu items
- Listing items with filters
- Retrieving item details
- Updating and deleting items
- Searching by name or description

This service ensures consistency and reusability across the application.
"""
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_current_user
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate, MenuItemRead
from app.controllers import menu_item_controller

router = APIRouter(prefix="/menu_items", tags=["menu_items"])

@router.post("/", response_model=MenuItemRead, status_code=status.HTTP_201_CREATED)
async def create_menu_item(
    item: MenuItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await menu_item_controller.create_menu_item(item, db, current_user)

@router.get("/{item_id}", response_model=MenuItemRead)
async def get_menu_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await menu_item_controller.get_menu_item(item_id, db, current_user)

@router.get("/", response_model=List[MenuItemRead])
async def list_menu_items(
    category_id: Optional[int] = None,
    vegetarian: Optional[bool] = None,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await menu_item_controller.list_menu_items(category_id, vegetarian, db, current_user)

@router.put("/{item_id}", response_model=MenuItemRead)
async def update_menu_item(
    item_id: int,
    item: MenuItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await menu_item_controller.update_menu_item(item_id, item, db, current_user)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    await menu_item_controller.delete_menu_item(item_id, db, current_user)
    return None

@router.get("/search/", response_model=List[MenuItemRead])
async def search_menu_items(
    query: str,
    db: AsyncSession = Depends(get_db)
):
    return await menu_item_controller.search_menu_items(query, db)
