"""
Review Controller

Handles user interactions related to submitting, retrieving, updating,
and deleting reviews for menu items or restaurants. Delegates logic to
the review_service module.
"""

from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import review_service
from app.schemas.review import ReviewCreate, ReviewUpdate, ReviewRead


async def create_review_controller(
    review_data: ReviewCreate,
    current_user,
    db: AsyncSession = Depends(),
) -> ReviewRead:
    """
    Submit a new review for a menu item or restaurant.
    Role: User
    """
    try:
        review_dict = review_data.dict()
        result = await review_service.create_review(review_dict, current_user, db)
        return ReviewRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def list_reviews_for_item_controller(
    item_id: int,
    db: AsyncSession = Depends(),
) -> List[ReviewRead]:
    """
    Get all reviews for a specific menu item.
    Role: Public
    """
    try:
        results = await review_service.list_reviews_for_item(item_id, db)
        return [ReviewRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def list_reviews_by_user_controller(
    user_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> List[ReviewRead]:
    """
    Get all reviews submitted by a specific user.
    Role: User
    """
    try:
        results = await review_service.list_reviews_by_user(user_id, current_user, db)
        return [ReviewRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_review_controller(
    review_id: int,
    db: AsyncSession = Depends(),
) -> ReviewRead:
    """
    Retrieve details of a single review by ID.
    Role: Public
    """
    try:
        result = await review_service.get_review(review_id, db)
        return ReviewRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def update_review_controller(
    review_id: int,
    review_data: ReviewUpdate,
    current_user,
    db: AsyncSession = Depends(),
) -> ReviewRead:
    """
    Update an existing review's content or rating.
    Role: User
    """
    try:
        update_dict = review_data.dict(exclude_unset=True)
        result = await review_service.update_review(review_id, update_dict, current_user, db)
        return ReviewRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_review_controller(
    review_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Delete a review by its ID.
    Role: User
    """
    try:
        return await review_service.delete_review(review_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
