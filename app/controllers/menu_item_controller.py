"""
Menu Item Controller

Handles incoming requests related to restaurant menu items and delegates
the business logic to the menu_service module.

Supports operations such as:
- Create, retrieve, update, delete menu items
- Filter by category or vegetarian
- Search by name or description

Role access: Admin (except public search).
"""

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.services import menu_service
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate, MenuItemRead
from fastapi.encoders import jsonable_encoder
from app.db.models.category import Category


async def create_menu_item(
    item_data: MenuItemCreate,
    db: AsyncSession,
    current_user
):
    """
    Create a new menu item (Admin only).
    """
    item = await menu_service.create_menu_item(db, item_data)
    # Eagerly fetch category to avoid greenlet error
    category_name = None
    if item.category_id:
        result = await db.execute(select(Category).where(Category.id == item.category_id))
        category = result.scalar_one_or_none()
        category_name = category.name if category else None
    tags = item.tags.split(',') if item.tags else []
    # Ensure required fields are not None
    response_data = {
        **item.__dict__,
        'category_name': category_name,
        'tags': tags,
        'preparation_time': item.preparation_time if item.preparation_time is not None else 0,
        'calories': item.calories if item.calories is not None else 0,
        'ingredients': item.ingredients if item.ingredients is not None else ''
    }
    response_data.pop('_sa_instance_state', None)
    return jsonable_encoder(response_data)


async def get_menu_item(
    item_id: int,
    db: AsyncSession,
    current_user
):
    """
    Retrieve a specific menu item by its ID (Admin only).
    """
    item = await menu_service.get_menu_item(db, item_id)
    # Eagerly fetch category to avoid greenlet error
    category_name = None
    if item.category_id:
        result = await db.execute(select(Category).where(Category.id == item.category_id))
        category = result.scalar_one_or_none()
        category_name = category.name if category else None
    tags = item.tags.split(',') if item.tags else []
    # Ensure required fields are not None
    response_data = {
        **item.__dict__,
        'category_name': category_name,
        'tags': tags,
        'preparation_time': item.preparation_time if item.preparation_time is not None else 0,
        'calories': item.calories if item.calories is not None else 0,
        'ingredients': item.ingredients if item.ingredients is not None else ''
    }
    response_data.pop('_sa_instance_state', None)
    return jsonable_encoder(response_data)


async def list_menu_items(
    category_id: int = None,
    vegetarian: bool = None,
    db: AsyncSession = None,
    current_user = None
):
    """
    List all menu items, optionally filtered by category or vegetarian flag (Admin only).
    """
    items = await menu_service.list_menu_items(db, category_id, vegetarian)
    response_data = []
    for item in items:
        # Eagerly fetch category to avoid greenlet error
        category_name = None
        if item.category_id:
            result = await db.execute(select(Category).where(Category.id == item.category_id))
            category = result.scalar_one_or_none()
            category_name = category.name if category else None
        tags = item.tags.split(',') if item.tags else []
        # Ensure required fields are not None
        item_data = {
            **item.__dict__,
            'category_name': category_name,
            'tags': tags,
            'preparation_time': item.preparation_time if item.preparation_time is not None else 0,
            'calories': item.calories if item.calories is not None else 0,
            'ingredients': item.ingredients if item.ingredients is not None else ''
        }
        item_data.pop('_sa_instance_state', None)
        response_data.append(jsonable_encoder(item_data))
    return response_data


async def update_menu_item(
    item_id: int,
    item_data: MenuItemUpdate,
    db: AsyncSession,
    current_user
):
    """
    Update an existing menu item (Admin only).
    """
    item = await menu_service.update_menu_item(db, item_id, item_data)
    # Eagerly fetch category to avoid greenlet error
    category_name = None
    if item.category_id:
        result = await db.execute(select(Category).where(Category.id == item.category_id))
        category = result.scalar_one_or_none()
        category_name = category.name if category else None
    tags = item.tags.split(',') if item.tags else []
    # Ensure required fields are not None
    response_data = {
        **item.__dict__,
        'category_name': category_name,
        'tags': tags,
        'preparation_time': item.preparation_time if item.preparation_time is not None else 0,
        'calories': item.calories if item.calories is not None else 0,
        'ingredients': item.ingredients if item.ingredients is not None else ''
    }
    response_data.pop('_sa_instance_state', None)
    return jsonable_encoder(response_data)


async def delete_menu_item(
    item_id: int,
    db: AsyncSession,
    current_user
):
    """
    Delete a menu item by ID (Admin only).
    """
    result = await menu_service.delete_menu_item(db, item_id)
    return result


async def search_menu_items(
    query: str,
    db: AsyncSession
):
    """
    Public search for menu items by name or description.
    """
    items = await menu_service.search_menu_items(db, query)
    response_data = []
    for item in items:
        # Eagerly fetch category to avoid greenlet error
        category_name = None
        if item.category_id:
            result = await db.execute(select(Category).where(Category.id == item.category_id))
            category = result.scalar_one_or_none()
            category_name = category.name if category else None
        tags = item.tags.split(',') if item.tags else []
        # Ensure required fields are not None
        item_data = {
            **item.__dict__,
            'category_name': category_name,
            'tags': tags,
            'preparation_time': item.preparation_time if item.preparation_time is not None else 0,
            'calories': item.calories if item.calories is not None else 0,
            'ingredients': item.ingredients if item.ingredients is not None else ''
        }
        item_data.pop('_sa_instance_state', None)
        response_data.append(jsonable_encoder(item_data))
    return response_data
