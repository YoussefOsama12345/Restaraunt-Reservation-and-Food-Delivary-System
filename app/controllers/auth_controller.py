"""
Auth Controller

Handles HTTP request-level logic for registration, login, token handling, and Firebase auth.
Delegates core logic to the `auth_service`.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def register_user(user_data, db):
    """
    Controller for registering a new user with email/password.
    """
    pass


def login_user(email, password, db):
    """
    Controller for logging in with email and password.
    Returns JWT token if successful.
    """
    pass


def login_with_oauth(firebase_token, db):
    """
    Controller for logging in via Firebase OAuth (Google/Facebook).
    """
    pass


def refresh_token(token):
    """
    Controller for refreshing access token from a valid refresh token.
    """
    pass
