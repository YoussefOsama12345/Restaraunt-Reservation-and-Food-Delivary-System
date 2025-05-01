"""
Auth Controller

Handles HTTP request-level logic for registration, login, token handling, and Firebase auth.
Delegates core logic to the `auth_service`.
"""

from app.services.auth_service import register_user as register_user_service, authenticate_user, login_or_register_oauth, create_access_token, decode_token
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
import asyncio

def register_user(user_data: UserCreate, db: Session):
    """
    Controller for registering a new user.
    Accepts a Pydantic UserCreate model and passes it to the service layer.
    """
    try:
        user = register_user_service(db, user_data)
        # Convert SQLAlchemy model to dict for response
        user_dict = {c.name: getattr(user, c.name) for c in user.__table__.columns}
        return user_dict
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Registration failed: {str(e)}")

async def login_user(identifier: str, password: str, db: AsyncSession):
    """
    Controller for logging in with email/username and password (ASYNC).
    Returns JWT token if successful.
    
    Args:
        identifier: Email or username
        password: Plain text password
        db: Async database session
        
    Returns:
        Dict with access token and token type
        
    Raises:
        HTTPException: If authentication fails
    """
    try:
        # Validate input
        if not identifier or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Email/username and password are required"
            )
            
        # Authenticate user
        user = await authenticate_user(db, identifier, password)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid credentials"
            )
            
        # Check if user is active
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="User account is inactive"
            )
            
        # Generate JWT token
        token_data = {
            "sub": str(user.id),
            "username": user.username,
            "role": user.role
        }
        access_token = create_access_token(token_data)
        
        # Return token response
        return {
            "access_token": access_token, 
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
            "role": user.role
        }
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log the error and raise a generic HTTP exception
        print(f"Login error: {str(e)}")
        import traceback
        print(traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )


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
