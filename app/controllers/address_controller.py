"""
User Controller

Handles user-related operations such as profile retrieval, updates,
admin user management, blocking, and deletion.
Delegates business logic to user_service or directly accesses the DB via SQLAlchemy.
"""

from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

# from app.db.database import get_db
# from app.api.deps import get_current_user, get_current_admin
# from app.db.models.user import User
# from app.schemas.user import UserRead, UserUpdate
# from app.services import user_service


def get_current_user_profile(
    current_user
):
    pass


def update_current_user_profile(
    user_update,
    db,
    current_user,
):
    pass


def list_all_users(
    db,
    current_admin,
):
    pass


def get_user_by_id(
    user_id,
    db,
    current_admin,
):
    pass


def block_user_account(
    user_id,
    db,
    current_admin,
):
    pass


def delete_user_account(
    user_id,
    db,
    current_admin,
):
    pass
