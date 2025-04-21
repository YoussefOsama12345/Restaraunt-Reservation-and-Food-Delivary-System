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
from sqlalchemy.orm import Session


def list_all_users(
    db: Session = Depends(),
    current_admin: Depends = Depends(),
) -> List[Depends]:
    """
    List all users in the system.
    Role: Admin
    """
    pass


def get_my_profile(
    current_user: Depends = Depends(),
) -> Depends:
    """
    Get the currently authenticated user's profile.
    Role: User
    """
    pass


def update_my_profile(
    user_update: Depends,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> Depends:
    """
    Update fields in the current user's profile.
    Role: User
    """
    pass


def get_user_by_id(
    user_id: int,
    db: Session = Depends(),
    current_admin: Depends = Depends(),
) -> Depends:
    """
    Retrieve a specific user's profile by ID.
    Role: Admin
    """
    pass


def block_user_account(
    user_id: int,
    db: Session = Depends(),
    current_admin: Depends = Depends(),
) -> Depends:
    """
    Block or deactivate a user account.
    Role: Admin
    """
    pass


def delete_user_account(
    user_id: int,
    db: Session = Depends(),
    current_admin: Depends = Depends(),
) -> dict:
    """
    Permanently delete a user account by ID.
    Role: Admin
    """
    pass
