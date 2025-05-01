"""
Handles operations related to user accounts, including retrieval of user profiles,
updating user information, listing users (admin-only), and managing account status.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.schemas.user import UserRead, UserUpdate, UserCreate
from app.api.deps import get_current_user, get_db, get_db_session
from app.controllers import user_controller
from app.services.auth_service import register_user

router = APIRouter(prefix="/users", tags=["users"])


def list_users():
    """
    List all registered users.
    Role: Admin
    """
    pass


def get_my_profile(current_user):
    """
    Get the profile of the currently authenticated user.
    Role: User
    """
    pass


def update_my_profile(user_update, current_user):
    """
    Update the authenticated user's profile.
    Role: User
    """
    pass


def get_user_by_id(user_id, current_user):
    """
    Retrieve a specific user's profile by user ID.
    Role: Admin
    """
    pass


def block_user(user_id, current_user):
    """
    Block a user account by user ID.
    Role: Admin
    """
    pass


def delete_user(user_id, current_user):
    """
    Delete a user account by user ID.
    Role: Admin
    """
    pass


def get_user_profile(current_user):
    """
    Get the profile of the currently authenticated user.
    Role: User
    """
    pass


@router.get("/", response_model=List[UserRead])
async def list_users(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    List all registered users.
    Role: Admin
    """
    # TODO: Add admin check logic here
    return await user_controller.list_users(db)


@router.get("/me", response_model=UserRead)
async def get_my_profile(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get the profile of the currently authenticated user.
    Role: User
    """
    return await user_controller.get_user_by_id(current_user.id, db)


@router.put("/me", response_model=UserRead)
async def update_my_profile(
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update the authenticated user's profile.
    Role: User
    """
    try:
        return await user_controller.update_user(current_user.id, user_update, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve a specific user's profile by user ID.
    Role: Admin
    """
    # TODO: Add admin check logic here
    return await user_controller.get_user_by_id(user_id, db)


@router.post("/{user_id}/block", response_model=UserRead)
async def block_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Block a user account by user ID.
    Role: Admin
    """
    # TODO: Add admin check logic here
    try:
        return await user_controller.block_user_account(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete a user account by user ID.
    Role: Admin
    """
    # TODO: Add admin check logic here
    try:
        return await user_controller.delete_user(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db_session)
):
    """
    Create a new user account.
    
    This endpoint allows creating users with different roles (customer, admin, driver).
    No authentication required - open for registration.
    
    Role: Public
    """
    try:
        # Use the register_user function from auth_service
        user = register_user(db, user_data)
        # Convert SQLAlchemy model to dict for Pydantic response
        user_dict = {c.name: getattr(user, c.name) for c in user.__table__.columns}
        return user_dict
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
