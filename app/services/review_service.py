"""
Review Service

Handles review and rating logic for menu items and restaurants.

Includes:
- Creating new reviews
- Retrieving individual reviews
- Listing reviews by menu item or user
- Updating reviews
- Deleting reviews

Role:
- User (create, update, delete, list own)
- Public (view specific reviews)
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.db.models.review import Review
from datetime import datetime
from typing import List, Dict

# Placeholder models and schemas
class ReviewCreate:
    item_id: int
    rating: float
    comment: str

class ReviewUpdate:
    rating: float
    comment: str


async def create_review(review_data: Dict, current_user, db: AsyncSession) -> Dict:
    """
    Create a new review for a restaurant or menu item.
    Role: User
    """
    # Check that the restaurant exists before creating the review
    restaurant_id = review_data.get('restaurant_id')
    if restaurant_id is not None:
        from app.services.restaurant_service import get_restaurant
        try:
            await get_restaurant(restaurant_id, db)
        except Exception:
            raise HTTPException(status_code=400, detail="Restaurant does not exist.")
    review_fields = {k: v for k, v in review_data.items() if k in Review.__table__.columns.keys()}
    review_fields['created_at'] = datetime.utcnow()
    review_fields['updated_at'] = datetime.utcnow()
    review_fields['user_id'] = current_user.id
    review = Review(**review_fields)
    db.add(review)
    await db.commit()
    await db.refresh(review)
    return {c.name: getattr(review, c.name) for c in Review.__table__.columns}


async def get_review(review_id: int, db: AsyncSession) -> Dict:
    """
    Retrieve a specific review by its ID.
    Role: Public
    """
    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalars().first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return {c.name: getattr(review, c.name) for c in Review.__table__.columns}


async def list_reviews_by_user(user_id: int, current_user, db: AsyncSession) -> List[Dict]:
    """
    List all reviews submitted by a specific user.
    Role: User
    """
    # Optionally: check if current_user is allowed to view user_id's reviews
    result = await db.execute(select(Review).where(Review.user_id == user_id))
    reviews = result.scalars().all()
    return [{c.name: getattr(r, c.name) for c in Review.__table__.columns} for r in reviews]


async def list_reviews_for_item(item_id: int, db: AsyncSession) -> List[Dict]:
    """
    List all reviews for a specific menu item.
    Role: Public
    """
    result = await db.execute(select(Review).where(Review.menu_item_id == item_id))
    reviews = result.scalars().all()
    return [{c.name: getattr(r, c.name) for c in Review.__table__.columns} for r in reviews]


async def update_review(review_id: int, update_data: Dict, current_user, db: AsyncSession) -> Dict:
    """
    Update an existing review.
    Role: User
    """
    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalars().first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    if review.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    for field, value in update_data.items():
        if field in Review.__table__.columns.keys() and value is not None and field != "user_id":
            setattr(review, field, value)
    review.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(review)
    return {c.name: getattr(review, c.name) for c in Review.__table__.columns}


async def delete_review(review_id: int, current_user, db: AsyncSession) -> Dict:
    """
    Delete a review by ID.
    Role: User
    """
    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalars().first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    if review.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    await db.delete(review)
    await db.commit()
    return {"detail": "Review deleted", "id": review_id}
