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
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

import firebase_admin
from firebase_admin import credentials, auth as firebase_auth

from app.security.jwt import get_password_hash as hash_password, verify_password as check_password, create_access_token as jwt_create_access_token, decode_access_token as jwt_decode_token
from app.db.models.user import User, UserRole
from app.schemas.user import UserCreate

# --------------------------- AUTHENTICATION UTILS --------------------------- #

def get_password_hash(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    Role: Internal
    """
    return hash_password(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hashed version.
    Role: Internal
    """
    return check_password(plain_password, hashed_password)


def register_user(db: Session, user_data: UserCreate) -> User:
    """
    Register a new user using email and password.
    Role: Public
    """
    try:
        user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
            full_name=getattr(user_data, "full_name", None),
            phone_number=getattr(user_data, "phone_number", None),
            is_active=True,
            role=UserRole.CUSTOMER,
            account_status="active",
            verification_status="unverified",
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or username already exists")
    except Exception as e:
        db.rollback()
        raise


async def authenticate_user(db: AsyncSession, identifier: str, password: str) -> Optional[User]:
    """
    Authenticate a user with email OR username and password (ASYNC).
    Role: Public
    """
    result = await db.execute(
        select(User).where((User.email == identifier) | (User.username == identifier))
    )
    user = result.scalars().first()
    print("User object:", user)
    if user:
        print("User dict:", getattr(user, "__dict__", str(user)))
        print("User attributes:", dir(user))
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# --------------------------- JWT SESSION MANAGEMENT --------------------------- #

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generate a JWT token with expiration.
    Role: Internal
    """
    return jwt_create_access_token(data, expires_delta)


def decode_token(token: str) -> Optional[dict]:
    """
    Decode a JWT token and validate its signature and expiration.
    Role: Internal
    """
    return jwt_decode_token(token)

# --------------------------- FIREBASE OAUTH AUTH --------------------------- #

def verify_oauth_token(id_token: str) -> dict:
    """
    Verify a Firebase ID token for OAuth (Google/Facebook).
    Role: Public
    """
    # TODO: Implement Firebase token verification
    return {}


def login_or_register_oauth(db: Session, firebase_data: dict) -> User:
    """
    Log in or auto-register a user using Firebase token data.
    Role: Public
    """
    # TODO: Implement login or auto-register using firebase_data
    user = User()
    user.email = firebase_data.get('email', 'test@example.com')
    user.id = 1  # Placeholder
    return user
