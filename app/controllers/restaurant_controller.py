"""
Restaurant Controller

Handles admin-level requests for creating, reading, updating, and deleting
restaurant branches or profiles. Delegates core logic to restaurant_service.
"""

from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import restaurant_service
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate, RestaurantRead


async def create_restaurant_controller(
    restaurant_data: RestaurantCreate,
    current_user,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Create a new restaurant branch or profile.
    Role: Admin
    """
    try:
        restaurant_dict = restaurant_data.dict()
        result = await restaurant_service.create_restaurant(restaurant_dict, current_user, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def create_restaurant(
    restaurant_data,
    current_user,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Create a new restaurant branch or profile.
    Role: Admin
    """
    try:
        # Accept both Pydantic model and dict, and do not call .dict() if already a dict
        if hasattr(restaurant_data, 'dict') and callable(restaurant_data.dict):
            restaurant_dict = restaurant_data.dict()
        else:
            restaurant_dict = dict(restaurant_data) if not isinstance(restaurant_data, dict) else restaurant_data
        result = await restaurant_service.create_restaurant(restaurant_dict, current_user, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_restaurant_controller(
    restaurant_id: int,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Retrieve a restaurant profile by its ID.
    Role: Admin
    """
    try:
        result = await restaurant_service.get_restaurant(restaurant_id, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def get_restaurant(
    restaurant_id: int,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Retrieve a restaurant profile by its ID.
    Role: Public
    """
    try:
        result = await restaurant_service.get_restaurant(restaurant_id, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def list_restaurants_controller(
    db: AsyncSession = Depends(),
) -> List[RestaurantRead]:
    """
    List all restaurants. Optionally filter by active status.
    Role: Admin
    """
    try:
        results = await restaurant_service.list_restaurants(db)
        return [RestaurantRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def list_restaurants(
    db: AsyncSession = Depends(),
) -> List[RestaurantRead]:
    """
    List all restaurants. Optionally filter by active status.
    Role: Admin
    """
    try:
        results = await restaurant_service.list_restaurants(db)
        # Ensure 'address' field is present for Pydantic validation
        for r in results:
            if 'address' not in r or r['address'] is None:
                r['address'] = ''  # or provide a sensible default
        return [RestaurantRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def update_restaurant_controller(
    restaurant_id: int,
    update_data: RestaurantUpdate,
    current_user,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Update an existing restaurant by ID.
    Role: Admin
    """
    try:
        update_dict = update_data.dict(exclude_unset=True)
        result = await restaurant_service.update_restaurant(restaurant_id, update_dict, current_user, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def update_restaurant(
    restaurant_id: int,
    update_data,
    current_user,
    db: AsyncSession = Depends(),
) -> RestaurantRead:
    """
    Update an existing restaurant by ID.
    Role: Admin
    """
    try:
        # Accept both Pydantic model and dict, and do not call .dict() if already a dict
        if hasattr(update_data, 'dict') and callable(update_data.dict):
            update_dict = update_data.dict(exclude_unset=True)
        else:
            update_dict = dict(update_data) if not isinstance(update_data, dict) else update_data
        result = await restaurant_service.update_restaurant(restaurant_id, update_dict, current_user, db)
        return RestaurantRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_restaurant_controller(
    restaurant_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Delete a restaurant from the system.
    Role: Admin
    """
    try:
        return await restaurant_service.delete_restaurant(restaurant_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_restaurant(
    restaurant_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Delete a restaurant from the system by ID.
    Role: Admin
    """
    try:
        return await restaurant_service.delete_restaurant(restaurant_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
