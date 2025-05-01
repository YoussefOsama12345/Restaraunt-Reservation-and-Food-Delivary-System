"""
Restaurant Management API Routes.

Provides endpoints for managing restaurant details and metadata.
Supports viewing, creating, updating, and deleting restaurants.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate, RestaurantRead
from app.api.deps import get_current_user, get_db
from app.controllers import restaurant_controller

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.post("/", response_model=RestaurantRead)
async def create_restaurant(
    restaurant_data: RestaurantCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Add a new restaurant entry to the system.
    Role: Admin
    """
    try:
        return await restaurant_controller.create_restaurant(restaurant_data, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[RestaurantRead])
async def list_restaurants(
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve a list of all available restaurants.
    Role: Public
    """
    try:
        return await restaurant_controller.list_restaurants(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{restaurant_id}", response_model=RestaurantRead)
async def get_restaurant(
    restaurant_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve information about a single restaurant by ID.
    Role: Public
    """
    try:
        return await restaurant_controller.get_restaurant(restaurant_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{restaurant_id}", response_model=RestaurantRead)
async def update_restaurant(
    restaurant_id: int,
    update_data: RestaurantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update restaurant metadata such as name, location, or contact info.
    Role: Admin
    """
    try:
        return await restaurant_controller.update_restaurant(restaurant_id, update_data, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{restaurant_id}", response_model=dict)
async def delete_restaurant(
    restaurant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete a restaurant from the system by ID.
    Role: Admin
    """
    try:
        return await restaurant_controller.delete_restaurant(restaurant_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
