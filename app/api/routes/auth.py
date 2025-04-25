"""
Authentication API routes.

Includes user login, registration, logout, password reset, and JWT-based authentication.
Supports email/password authentication and token refresh endpoints.
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.auth_controller import register_user as register_user_controller, login_user as login_user_controller, login_with_oauth as login_with_oauth_controller, refresh_token as refresh_token_controller
from app.api.deps import get_db
from app.schemas.user import UserCreate

router = APIRouter(tags=["auth"])


@router.post("/register")
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user_controller(user_data, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login_user(credentials: dict, db: AsyncSession = Depends(get_db)):
    identifier = credentials.get("email") or credentials.get("username")
    password = credentials.get("password")
    try:
        from app.controllers.auth_controller import login_user as login_user_controller
        return await login_user_controller(identifier, password, db)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login/oauth")
def login_oauth(firebase_token: str, db: Session = Depends(get_db)):
    return login_with_oauth_controller(firebase_token, db)


@router.post("/refresh")
def refresh_token(token: str):
    return refresh_token_controller(token)


@router.post("/forgot-password")
def forgot_password(email: str):
    # TODO: Implement forgot password logic
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/reset-password")
def reset_password(token: str, new_password: str):
    # TODO: Implement reset password logic
    raise HTTPException(status_code=501, detail="Not implemented")
