"""
Menu Service

Provides business logic for menu items, including:
- Creating new items
- Retrieving individual items
- Listing with optional filters
- Updating existing items
- Deleting items
- Searching by keyword

Role:
- Admin (create, update, delete)
- Public (view, list, search)
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, or_
from app.db.models.menu_item import MenuItem
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status

async def create_menu_item(db: AsyncSession, item_data: MenuItemCreate) -> MenuItem:
    # Check for duplicate menu item name
    result = await db.execute(select(MenuItem).where(MenuItem.name == item_data.name))
    existing_item = result.scalar_one_or_none()
    if existing_item:
        raise HTTPException(status_code=400, detail="Menu item with this name already exists.")
    fields = {c.name for c in MenuItem.__table__.columns}
    data = {k: v for k, v in item_data.dict().items() if k in fields}
    # Serialize tags list to comma-separated string
    if 'tags' in data and isinstance(data['tags'], list):
        data['tags'] = ','.join(data['tags'])
    new_item = MenuItem(**data)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

async def get_menu_item(db: AsyncSession, item_id: int) -> MenuItem:
    result = await db.execute(select(MenuItem).where(MenuItem.id == item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found.")
    return item

async def list_menu_items(db: AsyncSession, category_id: int = None, vegetarian: bool = None) -> list:
    query = select(MenuItem)
    if category_id is not None:
        query = query.where(MenuItem.category_id == category_id)
    if vegetarian is not None:
        query = query.where(MenuItem.is_vegetarian == vegetarian)
    result = await db.execute(query)
    return result.scalars().all()

async def update_menu_item(db: AsyncSession, item_id: int, item_data: MenuItemUpdate) -> MenuItem:
    result = await db.execute(select(MenuItem).where(MenuItem.id == item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found.")
    fields = {c.name for c in MenuItem.__table__.columns}
    update_data = item_data.dict(exclude_unset=True)
    if 'tags' in update_data and isinstance(update_data['tags'], list):
        update_data['tags'] = ','.join(update_data['tags'])
    for field, value in update_data.items():
        if field in fields:
            setattr(item, field, value)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A menu item with this name already exists."
        )
    await db.refresh(item)
    return item

async def delete_menu_item(db: AsyncSession, item_id: int) -> dict:
    result = await db.execute(select(MenuItem).where(MenuItem.id == item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found.")
    await db.delete(item)
    await db.commit()
    return {"detail": "Menu item deleted."}

async def search_menu_items(db: AsyncSession, query: str) -> list:
    stmt = select(MenuItem).where(
        or_(MenuItem.name.ilike(f"%{query}%"), MenuItem.description.ilike(f"%{query}%"))
    )
    result = await db.execute(stmt)
    return result.scalars().all()
