"""
User Service

Handles business logic for user profile management:
- View and update user profile
- List users (admin)
- Block or delete users (admin)
"""

from typing import List, Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.db.models.user import User
from datetime import datetime

class UserUpdate:
    email: Optional[str]
    password: Optional[str]

async def list_users(db: AsyncSession) -> List[dict]:
    """
    List all users in the system.
    Role: Admin
    """
    result = await db.execute(select(User))
    users = result.scalars().all()
    user_dicts = []
    for u in users:
        user_data = {c.name: getattr(u, c.name) for c in User.__table__.columns}
        # Ensure created_at and updated_at are not None, set to epoch if missing
        if user_data.get("created_at") is None:
            user_data["created_at"] = datetime(1970, 1, 1)
        if user_data.get("updated_at") is None:
            user_data["updated_at"] = datetime(1970, 1, 1)
            
        # Ensure boolean fields are not None
        if user_data.get("is_active") is None:
            user_data["is_active"] = True
        if user_data.get("is_admin") is None:
            user_data["is_admin"] = False
        user_dicts.append(user_data)
    return user_dicts

async def get_user_by_id(user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve a user by their ID.
    Role: Admin
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user_data = {c.name: getattr(user, c.name) for c in User.__table__.columns}
    if user_data.get("created_at") is None:
        user_data["created_at"] = datetime(1970, 1, 1)
    if user_data.get("updated_at") is None:
        user_data["updated_at"] = datetime(1970, 1, 1)
    return user_data

async def update_user_profile(user_id: int, update_data: UserUpdate, db: AsyncSession) -> dict:
    """
    Update the profile of a user.
    Role: User
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Check if username is being updated and if it's already taken
    if hasattr(update_data, 'username') and update_data.username is not None and update_data.username != user.username:
        # Check if username already exists
        username_check = await db.execute(select(User).where(User.username == update_data.username))
        existing_user = username_check.scalars().first()
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username '{update_data.username}' is already taken"
            )
    
    # Check if email is being updated and if it's already taken
    if hasattr(update_data, 'email') and update_data.email is not None and update_data.email != user.email:
        # Check if email already exists
        email_check = await db.execute(select(User).where(User.email == update_data.email))
        existing_user = email_check.scalars().first()
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{update_data.email}' is already registered"
            )
    
    # Update user fields
    for field, value in update_data.dict(exclude_unset=True).items():
        if field in User.__table__.columns.keys() and value is not None:
            setattr(user, field, value)
    
    user.updated_at = datetime.utcnow()
    try:
        await db.commit()
        await db.refresh(user)
        return {c.name: getattr(user, c.name) for c in User.__table__.columns}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

async def update_user(user_id: int, update_data: Dict, db: AsyncSession) -> dict:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Check if username is being updated and if it's already taken
    if 'username' in update_data and update_data['username'] is not None and update_data['username'] != user.username:
        # Check if username already exists
        username_check = await db.execute(select(User).where(User.username == update_data['username']))
        existing_user = username_check.scalars().first()
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username '{update_data['username']}' is already taken"
            )
    
    # Check if email is being updated and if it's already taken
    if 'email' in update_data and update_data['email'] is not None and update_data['email'] != user.email:
        # Check if email already exists
        email_check = await db.execute(select(User).where(User.email == update_data['email']))
        existing_user = email_check.scalars().first()
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{update_data['email']}' is already registered"
            )
    
    # Only update fields that are real columns
    for field, value in update_data.items():
        if field in User.__table__.columns.keys() and value is not None:
            setattr(user, field, value)
            
    user.updated_at = datetime.utcnow()
    try:
        await db.commit()
        await db.refresh(user)
        user_data = {c.name: getattr(user, c.name) for c in User.__table__.columns}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if user_data.get("created_at") is None:
        user_data["created_at"] = datetime(1970, 1, 1)
    if user_data.get("updated_at") is None:
        user_data["updated_at"] = datetime(1970, 1, 1)
    return user_data

async def block_user(user_id: int, db: AsyncSession) -> dict:
    """
    Block or deactivate a user.
    Role: Admin
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.account_status = "blocked"
    await db.commit()
    await db.refresh(user)
    return {c.name: getattr(user, c.name) for c in User.__table__.columns}

async def delete_user(user_id: int, db: AsyncSession) -> dict:
    """
    Permanently delete a user from the system.
    Role: Admin
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"detail": "User deleted", "id": user_id}
