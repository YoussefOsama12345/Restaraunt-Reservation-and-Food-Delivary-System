"""
User Module

This module defines the `User` model for the Restaurant Management System (RMS).
The `User` model represents users in the system, such as admin, staff, and other types of users.
It includes essential user details such as username, role, password, and timestamps for account creation.

Models:
-------
- User: Represents a user in the RMS, including their authentication details and role.

Usage:
------
The `User` model is used to manage user accounts, roles, and authentication in the system.
It supports storing essential user information for login, account management, and access control.
"""

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class User(Base):
    """
    User model stores information about users (e.g., admin, staff) in the system, including authentication details.
    """
    __tablename__ = "users"

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"
