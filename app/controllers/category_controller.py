"""
Category Controller

Handles requests related to food category operations like creation, retrieval,
update, and deletion. Delegates business logic to the `category_service`.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import category_service
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from typing import List


# Role : Admin
async def create_category(
    category_data: CategoryCreate,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends()
):
    """
    Create a new food category.

    Role: Admin
    """
    cat = await category_service.create_category(db, category_data)
    return CategoryRead.from_orm(cat)


async def list_categories(
    db: AsyncSession = Depends()
):
    """
    Retrieve all food categories.

    Role: Public
    """
    cats = await category_service.list_categories(db)
    # Patch: replace None with 0 for fields that can't be None in the response model
    def patch(cat):
        patched = cat
        if getattr(patched, 'display_order', None) is None:
            patched.display_order = 0
        if getattr(patched, 'item_count', None) is None:
            patched.item_count = 0
        if getattr(patched, 'total_sales', None) is None:
            patched.total_sales = 0.0
        return patched
    return [CategoryRead.from_orm(patch(cat)) for cat in cats]


async def get_category_by_id(
    category_id: int,
    db: AsyncSession = Depends()
):
    """
    Retrieve a single category by its ID.

    Role: Public
    """
    cat = await category_service.get_category(db, category_id)
    # Patch: replace None with 0 for fields that can't be None in the response model
    if getattr(cat, 'display_order', None) is None:
        cat.display_order = 0
    if getattr(cat, 'item_count', None) is None:
        cat.item_count = 0
    if getattr(cat, 'total_sales', None) is None:
        cat.total_sales = 0.0
    return CategoryRead.from_orm(cat)


# Role : Admin
async def update_category(
    category_id: int,
    update_data: CategoryUpdate,
    db: AsyncSession = Depends(),
    current_user: Depends = Depends()
):
    """
    Update an existing category's information.

    Role: Admin
    """
    cat = await category_service.update_category(db, category_id, update_data)
    # Patch: replace None with 0 for fields that can't be None in the response model
    if getattr(cat, 'display_order', None) is None:
        cat.display_order = 0
    if getattr(cat, 'item_count', None) is None:
        cat.item_count = 0
    if getattr(cat, 'total_sales', None) is None:
        cat.total_sales = 0.0
    return CategoryRead.from_orm(cat)


# Role : Admin
async def delete_category(
    category_id: int, 
    db: AsyncSession = Depends(), 
    current_user: Depends = Depends(), 
    force: bool = False
):
    """
    Delete a category by its ID.

    Role: Admin
    """
    return await category_service.delete_category(db, category_id, force)
