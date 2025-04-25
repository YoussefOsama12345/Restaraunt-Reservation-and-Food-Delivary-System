"""
Defines common dependencies for API endpoints, including:
- Database session (get_db)
- OAuth2 password bearer token scheme
- Current user retrieval and role-based access control
"""
# ---
# UPDATED BY AI: Improved get_current_user to support async DB access, robust JWT extraction/validation, and debug logging.
# Ensured admin dependency checks user role correctly for FastAPI security.
# ---
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.db.models.user import User, UserRole
from app.security.jwt import decode_access_token

bearer_scheme = HTTPBearer()

async def get_current_user(credentials: str = Depends(bearer_scheme), db: AsyncSession = Depends(get_db)) -> User:
    """
    Retrieve the current authenticated user based on JWT token (HTTP Bearer).
    Raises HTTP 401 if token is invalid or user not found.
    """
    print("DEBUG: deps.py get_current_user called")
    print("DEBUG: credentials:", credentials)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = credentials.credentials
        if token.startswith("Bearer "):
            token = token[len("Bearer ") :]
        print("DEBUG: token:", token)
        payload = decode_access_token(token)
        print("DEBUG: payload:", payload)
        user_id: int = int(payload.get("sub"))
    except Exception as e:
        print("DEBUG: Exception in get_current_user:", e)
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    print("DEBUG: user:", user)
    if not user:
        raise credentials_exception
    return user

def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency that ensures the current user has admin privileges.

    Raises HTTP 403 if user is not an admin.
    """
    if current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user

def get_current_delivery(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency that ensures the current user has delivery staff privileges.

    Raises HTTP 403 if user is not delivery personnel.
    """
    if current_user.role != UserRole.delivery:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Delivery privileges required"
        )
    return current_user
