"""
Auth Controller

Handles HTTP request-level logic for registration, login, token handling, and Firebase auth.
Delegates core logic to the `auth_service`.
"""

from app.services.auth_service import register_user as register_user_service, authenticate_user, login_or_register_oauth, create_access_token, decode_token
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
import asyncio

def register_user(user_data: dict, db: Session):
    try:
        user = register_user_service(db, user_data)
        return {"id": user.id, "email": user.email}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Registration failed: {e}")

async def login_user(identifier: str, password: str, db: Session):
    """
    Controller for logging in with email/username and password (ASYNC).
    Returns JWT token if successful.
    """
    user = await authenticate_user(db, identifier, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


def login_with_oauth(firebase_token: str, db: Session):
    """
    Controller for logging in via Firebase OAuth (Google/Facebook).
    """
    try:
        firebase_data = {}  # TODO: Verify token and extract user info
        user = login_or_register_oauth(db, firebase_data)
        access_token = create_access_token({"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="OAuth authentication failed")


def refresh_token(token: str):
    """
    Controller for refreshing access token from a valid refresh token.
    """
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    new_token = create_access_token({"sub": payload.get("sub")})
    return {"access_token": new_token, "token_type": "bearer"}
