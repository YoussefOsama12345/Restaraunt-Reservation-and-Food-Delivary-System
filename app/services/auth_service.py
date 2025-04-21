"""
Authentication service for user management and login.

This module supports two authentication types:
- Email/password authentication (custom backend)
- Google/Facebook login via Firebase OAuth (using Firebase Admin SDK)

Also includes functionality for:
- JWT access token generation and validation
- Password hashing and verification
- Auto-registration of users via Firebase OAuth login
"""

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

import firebase_admin
from firebase_admin import credentials, auth as firebase_auth

# -------------------------------------------------------------------------
# Placeholder User and UserCreate classes to decouple from external folders
# -------------------------------------------------------------------------

class User:
    id: int
    email: str
    hashed_password: str
    # Add any other required fields here


class UserCreate:
    email: str
    password: str
    # Add any other required fields here

# --------------------------- AUTHENTICATION UTILS --------------------------- #

def get_password_hash(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    Role: Internal
    """
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hashed version.
    Role: Internal
    """
    pass


def register_user(db: Session, user_data: UserCreate) -> User:
    """
    Register a new user using email and password.
    Role: Public
    """
    pass


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """
    Authenticate a user with email and password.
    Role: Public
    """
    pass

# --------------------------- JWT SESSION MANAGEMENT --------------------------- #

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generate a JWT token with expiration.
    Role: Internal
    """
    pass


def decode_token(token: str) -> Optional[dict]:
    """
    Decode a JWT token and validate its signature and expiration.
    Role: Internal
    """
    pass

# --------------------------- FIREBASE OAUTH AUTH --------------------------- #

def verify_oauth_token(id_token: str) -> dict:
    """
    Verify a Firebase ID token for OAuth (Google/Facebook).
    Role: Public
    """
    pass


def login_or_register_oauth(db: Session, firebase_data: dict) -> User:
    """
    Log in or auto-register a user using Firebase token data.
    Role: Public
    """
    pass
