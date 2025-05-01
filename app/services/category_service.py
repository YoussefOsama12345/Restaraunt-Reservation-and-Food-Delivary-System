"""
Category Service

Handles business logic related to food menu categories.

Includes:
- Creating new categories
- Retrieving individual category details
- Listing all categories
- Updating category information
- Deleting a category

Roles:
- Admin: Create, update, delete
- Public: List and retrieve
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.db.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


async def create_category(db: AsyncSession, category_data: CategoryCreate) -> Category:
    """
    Create a new menu category.
    Role: Admin
    """
    result = await db.execute(select(Category).where(Category.name == category_data.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Category with this name already exists.")
    # Exclude 'model_config' and any other Pydantic-only fields
    data = {k: v for k, v in category_data.dict(exclude_unset=True).items() if k in Category.__table__.columns.keys()}
    new_cat = Category(**data)
    db.add(new_cat)
    await db.commit()
    await db.refresh(new_cat)
    return new_cat


async def get_category(db: AsyncSession, category_id: int) -> Category:
    """
    Retrieve a category by its ID.
    Role: Public
    """
    result = await db.execute(select(Category).where(Category.id == category_id))
    cat = result.scalar_one_or_none()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found.")
    return cat


async def list_categories(db: AsyncSession) -> List[Category]:
    """
    Retrieve a list of all categories.
    Role: Public
    """
    result = await db.execute(select(Category))
    return result.scalars().all()


async def update_category(db: AsyncSession, category_id: int, update_data: CategoryUpdate) -> Category:
    """
    Update an existing category.
    Role: Admin
    """
    category = await db.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    # Check for duplicate name if name is being updated
    if update_data.name and update_data.name != category.name:
        result = await db.execute(select(Category).where(Category.name == update_data.name))
        existing = result.scalar_one_or_none()
        if existing:
            raise HTTPException(status_code=400, detail="Category with this name already exists.")
    # Only update fields that are set
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(category, field, value)
    await db.commit()
    await db.refresh(category)
    return category


async def delete_category(db: AsyncSession, category_id: int, force: bool = False) -> dict:
    category = await db.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    from app.db.models.menu_item import MenuItem
    from app.db.models.cart import CartItem
    from app.db.models.order_item import OrderItem
    from app.db.models.review import Review
    # Find all menu items for this category
    menu_items = await db.execute(select(MenuItem).where(MenuItem.category_id == category_id))
    menu_items = menu_items.scalars().all()
    if not force:
        # For each menu item, check for cart items
        for item in menu_items:
            cart_items = await db.execute(select(CartItem).where(CartItem.menu_item_id == item.id))
            cart_items = cart_items.scalars().all()
            if cart_items:
                raise HTTPException(status_code=400, detail="Cannot delete category: there are cart items referencing its menu items.")
    else:
        # If force, delete all cart items, order items, and reviews referencing these menu items (in bulk)
        menu_item_ids = [item.id for item in menu_items]
        if menu_item_ids:
            await db.execute(CartItem.__table__.delete().where(CartItem.menu_item_id.in_(menu_item_ids)))
            await db.execute(OrderItem.__table__.delete().where(OrderItem.menu_item_id.in_(menu_item_ids)))
            await db.execute(Review.__table__.delete().where(Review.menu_item_id.in_(menu_item_ids)))
            await db.execute(MenuItem.__table__.delete().where(MenuItem.id.in_(menu_item_ids)))
            await db.flush()
    # Now reload the category from DB to ensure it's not attached to any menu_items
    await db.refresh(category)
    await db.delete(category)
    await db.commit()
    return {"detail": "Category deleted successfully."}
