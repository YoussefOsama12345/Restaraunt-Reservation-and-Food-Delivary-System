"""
User Controller

Handles business logic for managing user accounts:
- List users (admin)
- Get/update personal profile
- Get user by ID (admin)
- Block or delete user accounts

Delegates logic to user_service.
"""

from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import user_service
from app.schemas.user import UserRead, UserUpdate
from app.utils.model_helpers import prepare_user_data_for_pydantic


# Renamed from list_all_users to list_users for consistency with route usage
async def list_users(
    db: AsyncSession = Depends(),
) -> List[UserRead]:
    """
    List all users in the system.
    Role: Admin
    """
    try:
        users = await user_service.list_users(db)
        # Prepare user data before passing to Pydantic model
        prepared_users = [prepare_user_data_for_pydantic(u) for u in users]
        return [UserRead(**u) for u in prepared_users]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_my_profile(
    db: AsyncSession = Depends(),
) -> UserRead:
    """
    Get the currently authenticated user's profile.
    Role: User
    """
    try:
        user = await user_service.get_current_user(db)
        # Prepare user data before passing to Pydantic model
        prepared_user = prepare_user_data_for_pydantic(user)
        return UserRead(**prepared_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def update_my_profile(
    user_update: UserUpdate,
    db: AsyncSession = Depends(),
) -> UserRead:
    """
    Update fields in the current user's profile.
    Role: User
    """
    try:
        result = await user_service.update_current_user(user_update.dict(exclude_unset=True), db)
        return UserRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(),
) -> UserRead:
    """
    Retrieve a specific user's profile by ID.
    Role: Admin
    """
    try:
        user = await user_service.get_user_by_id(user_id, db)
        return UserRead(**user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession,
) -> UserRead:
    """
    Update a user's profile by user ID.
    Role: Admin/User
    """
    try:
        result = await user_service.update_user(user_id, user_update.dict(exclude_unset=True), db)
        return UserRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def block_user_account(
    user_id: int,
    db: AsyncSession = Depends(),
) -> UserRead:
    """
    Block or deactivate a user account.
    Role: Admin
    """
    try:
        result = await user_service.block_user(user_id, db)
        return UserRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_user(
    user_id: int,
    db: AsyncSession,
) -> dict:
    """
    Permanently delete a user account by ID.
    Role: Admin
    """
    try:
        return await user_service.delete_user(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_user_account(
    user_id: int,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Permanently delete a user account by ID.
    Role: Admin
    """
    try:
        return await user_service.delete_user(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
