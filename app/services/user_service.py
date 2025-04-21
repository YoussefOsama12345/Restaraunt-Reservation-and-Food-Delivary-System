"""
User Service

Handles business logic for user profile management:
- View and update user profile
- List users (admin)
- Block or delete users (admin)
"""

from typing import List, Optional
from sqlalchemy.orm import Session
# Placeholder model and schema
class User:
    id: int
    email: str
    is_active: bool

class UserUpdate:
    email: Optional[str]
    password: Optional[str]

def list_users() -> List[User]:
    """
    List all users in the system.
    Role: Admin
    """
    pass

def get_user_by_id(user_id: int) -> User:
    """
    Retrieve a user by their ID.
    Role: Admin
    """
    pass

def update_user_profile(user_id: int, update_data: UserUpdate) -> User:
    """
    Update the profile of a user.
    Role: User
    """
    pass

def block_user(user_id: int) -> User:
    """
    Block or deactivate a user.
    Role: Admin
    """
    pass

def delete_user(user_id: int) -> dict:
    """
    Permanently delete a user from the system.
    Role: Admin
    """
    pass
