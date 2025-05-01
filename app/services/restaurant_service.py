"""
Restaurant Service

Provides business logic for managing restaurant information including
creation, updates, retrieval, deletion, and optional search/filter functionality.

Use Cases:
- Admins can create and manage restaurants
- Public users can view/search restaurants
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.db.models.restaurant import Restaurant
from datetime import datetime

class RestaurantCreate:
    name: str
    address: str

class RestaurantUpdate:
    name: Optional[str]
    address: Optional[str]


async def create_restaurant(restaurant_data, current_user, db: AsyncSession) -> dict:
    if hasattr(restaurant_data, 'dict') and callable(restaurant_data.dict):
        data = restaurant_data.dict()
    else:
        data = dict(restaurant_data) if not isinstance(restaurant_data, dict) else restaurant_data
    from app.db.models.restaurant import Restaurant
    # Only keep fields that are actual columns in the Restaurant table
    valid_fields = {k: v for k, v in data.items() if k in Restaurant.__table__.columns.keys()}
    # 'address' is NOT a valid column, but 'location' is. Map if needed.
    if 'location' not in valid_fields or valid_fields['location'] is None:
        # Accept 'address' as an alias for 'location' if present
        if 'address' in data and data['address'] is not None:
            valid_fields['location'] = data['address']
        else:
            valid_fields['location'] = ''
    import datetime
    if 'created_at' not in valid_fields or valid_fields['created_at'] is None:
        valid_fields['created_at'] = datetime.datetime.utcnow()
    if 'updated_at' not in valid_fields or valid_fields['updated_at'] is None:
        valid_fields['updated_at'] = datetime.datetime.utcnow()
    restaurant = Restaurant(**valid_fields)
    db.add(restaurant)
    await db.commit()
    await db.refresh(restaurant)
    result = {c.name: getattr(restaurant, c.name) for c in Restaurant.__table__.columns}
    # Always include 'address' in the result for RestaurantRead compatibility
    result['address'] = result.get('location', '')
    return result


async def get_restaurant(restaurant_id: int, db: AsyncSession) -> dict:
    from app.db.models.restaurant import Restaurant
    result = await db.execute(
        Restaurant.__table__.select().where(Restaurant.id == restaurant_id)
    )
    restaurant = result.fetchone()
    if not restaurant:
        raise Exception("Restaurant not found")
    # Convert SQLAlchemy Row to dict
    restaurant_dict = dict(restaurant._mapping)
    # Always include 'address' in the returned dict for RestaurantRead compatibility
    restaurant_dict['address'] = restaurant_dict.get('location', '')
    return restaurant_dict


async def list_restaurants(db: AsyncSession) -> List[dict]:
    """
    List all available restaurants.
    Role: Public
    """
    result = await db.execute(select(Restaurant))
    restaurants = result.scalars().all()
    return [{c.name: getattr(r, c.name) for c in Restaurant.__table__.columns} for r in restaurants]


async def update_restaurant(restaurant_id: int, update_data, current_user, db: AsyncSession) -> dict:
    from app.db.models.restaurant import Restaurant
    # Accept both dict and Pydantic model, never call .dict() on a dict
    if hasattr(update_data, 'dict') and callable(update_data.dict):
        data = update_data.dict(exclude_unset=True)
    else:
        data = dict(update_data) if not isinstance(update_data, dict) else update_data
    # Only keep fields that are actual columns in the Restaurant table
    valid_fields = {k: v for k, v in data.items() if k in Restaurant.__table__.columns.keys()}
    # Map address to location if present
    if 'address' in data and ('location' not in valid_fields or not valid_fields['location']):
        valid_fields['location'] = data['address']
    result = await db.execute(Restaurant.__table__.select().where(Restaurant.id == restaurant_id))
    restaurant_row = result.fetchone()
    if not restaurant_row:
        raise Exception("Restaurant not found")
    # Fetch ORM object for update
    restaurant = await db.get(Restaurant, restaurant_id)
    for field, value in valid_fields.items():
        setattr(restaurant, field, value)
    import datetime
    restaurant.updated_at = datetime.datetime.utcnow()
    await db.commit()
    await db.refresh(restaurant)
    result = {c.name: getattr(restaurant, c.name) for c in Restaurant.__table__.columns}
    # Always include 'address' in the result for RestaurantRead compatibility
    result['address'] = result.get('location', '')
    return result


async def delete_restaurant(restaurant_id: int, current_user, db: AsyncSession) -> dict:
    """
    Delete a restaurant entry.
    Role: Admin
    """
    result = await db.execute(select(Restaurant).where(Restaurant.id == restaurant_id))
    restaurant = result.scalars().first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    await db.delete(restaurant)
    await db.commit()
    return {"detail": "Restaurant deleted", "id": restaurant_id}


async def search_restaurants(query: str, db: AsyncSession) -> List[dict]:
    """
    Search restaurants by name or location.
    Role: Public
    """
    # TO DO: implement search functionality
    pass
