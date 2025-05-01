"""
Address Controller

Manages address book operations for authenticated users, including:
- Creating new addresses
- Listing saved addresses
- Updating existing addresses
- Deleting addresses
- Retrieving the default address

Delegates business logic to address_service.

Access: All endpoints require authenticated users.
"""

from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from typing import List
from app.api.deps import get_db, get_current_user
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.controllers import category_controller
from app.db.database import get_db
from app.db.models.category import Category

router = APIRouter(tags=["categories"])

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await category_controller.create_category(category_data, db, current_user)

@router.get("/", response_model=List[CategoryRead])
async def list_categories(
    db: AsyncSession = Depends(get_db)
):
    return await category_controller.list_categories(db)

@router.get("/{category_id}", response_model=CategoryRead)
async def get_category_by_id(
    category_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await category_controller.get_category_by_id(category_id, db)

@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(
    category_id: int,
    update_data: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await category_controller.update_category(category_id, update_data, db, current_user)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    force: bool = Query(False, description="Force delete all related cart items and menu items"),
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    await category_controller.delete_category(category_id, db, current_user, force)
    return None

@router.post("/fix-null-fields", tags=["categories"], include_in_schema=True)
async def fix_null_category_fields(db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    # Only allow admin (add your admin check here if needed)
    await db.execute(update(Category).where(Category.display_order == None).values(display_order=0))
    await db.execute(update(Category).where(Category.item_count == None).values(item_count=0))
    await db.execute(update(Category).where(Category.total_sales == None).values(total_sales=0.0))
    await db.commit()
    return {"detail": "Null fields fixed."}
