"""
Review and Rating API routes.

This module provides RESTful API endpoints for managing user-submitted reviews
for restaurants and menu items. Users can:
- Submit reviews with ratings and comments
- Retrieve reviews by item, user, or ID
- Update existing reviews
- Delete reviews

All write operations require authentication.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.review import ReviewCreate, ReviewUpdate, ReviewRead
from app.api.deps import get_current_user, get_db
from app.controllers import review_controller

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=ReviewRead)
async def create_review(
    review_data: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Submit a new review.
    Role: User
    """
    try:
        return await review_controller.create_review_controller(review_data, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/item/{item_id}", response_model=List[ReviewRead])
async def list_reviews_for_item(
    item_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve all reviews for a specific menu item.
    Role: Public
    """
    try:
        return await review_controller.list_reviews_for_item_controller(item_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/user/{user_id}", response_model=List[ReviewRead])
async def list_reviews_by_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve all reviews submitted by a specific user.
    Role: User
    """
    try:
        return await review_controller.list_reviews_by_user_controller(user_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{review_id}", response_model=ReviewRead)
async def get_review(
    review_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve a single review by its ID.
    Role: Public
    """
    try:
        return await review_controller.get_review_controller(review_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{review_id}", response_model=ReviewRead)
async def update_review(
    review_id: int,
    review_data: ReviewUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update an existing review.
    Role: User
    """
    try:
        return await review_controller.update_review_controller(review_id, review_data, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{review_id}", response_model=dict)
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete a review by its ID.
    Role: User
    """
    try:
        return await review_controller.delete_review_controller(review_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
