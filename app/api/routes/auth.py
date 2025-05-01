"""
Authentication API routes.

Includes user login, registration, logout, password reset, and JWT-based authentication.
Supports email/password authentication and token refresh endpoints.
"""
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.controllers.auth_controller import register_user as register_user_controller, login_user as login_user_controller, login_with_oauth as login_with_oauth_controller, refresh_token as refresh_token_controller
from app.api.deps import get_db, get_db_session
from app.schemas.user import UserCreate, UserRead
from app.services.user_registration import create_user

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=Dict[str, Any], status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate):
    """
    Register a new user with email, username, and password.
    
    This endpoint allows creating users with different roles (customer, admin, driver).
    No authentication required - open for registration.
    """
    try:
        # Import the direct registration function here to avoid circular imports
        from direct_user_registration import register_user_direct
        
        # Validate required fields
        if not user_data.username or not user_data.email or not user_data.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username, email, and password are required"
            )
        
        # Use the direct registration function to avoid async/sync issues
        result = register_user_direct(user_data)
        print(f"User registration result: {result}")
        return result
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise e
    except Exception as e:
        # Log the error and raise a generic HTTP exception
        import traceback
        print(f"Registration error: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Registration failed: {str(e)}")


@router.post("/register-old")
def register_user_old(user_data: UserCreate, db: Session = Depends(get_db_session)):
    """
    Legacy registration endpoint - may have issues with async/sync mixing.
    """
    try:
        return register_user_controller(user_data, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


class LoginRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str

@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(credentials: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    Login with username/email and password.
    Returns a JWT token if successful.
    
    Request body:
    {
        "username": "string" or "email": "string",
        "password": "string"
    }
    
    Returns:
    {
        "access_token": "string",
        "token_type": "bearer",
        "user_id": int,
        "username": "string",
        "role": "string"
    }
    """
    print("\n===== LOGIN ENDPOINT DEBUG =====")
    print(f"Received credentials: {credentials}")
    
    # Get identifier (email or username) and password from request
    identifier = credentials.email or credentials.username
    password = credentials.password
    
    print(f"Extracted identifier: '{identifier}'")
    print(f"Password received: '{password}'")
    
    # Validate input
    if not identifier:
        print("Error: Missing identifier (email or username)")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email or username is required"
        )
    if not password:
        print("Error: Missing password")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Password is required"
        )
    
    print(f"Login attempt for user: '{identifier}'")
    
    try:
        # Try direct authentication first for debugging
        print("Attempting direct authentication...")
        from app.services.auth_service import authenticate_user
        user = await authenticate_user(db, identifier, password)
        
        if user:
            print(f"Direct authentication successful for user: {user.username}")
            # Generate token manually
            from app.security.jwt import create_access_token
            token_data = {
                "sub": str(user.id),
                "username": user.username,
                "role": user.role
            }
            access_token = create_access_token(token_data)
            
            # Return token response
            result = {
                "access_token": access_token, 
                "token_type": "bearer",
                "user_id": user.id,
                "username": user.username,
                "role": user.role
            }
            print(f"Login successful, returning token")
            return result
        else:
            print("Direct authentication failed")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid credentials"
            )
    except HTTPException as e:
        # Re-raise HTTP exceptions
        print(f"HTTP Exception: {e.detail}")
        raise e
    except Exception as e:
        import traceback
        print(f"Login error: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Login failed: {str(e)}"
        )


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

def reset_password(token: str, new_password: str):
    # TODO: Implement reset password logic
    raise HTTPException(status_code=501, detail="Not implemented")

def reset_password(token: str, new_password: str):
    # TODO: Implement reset password logic
    raise HTTPException(status_code=501, detail="Not implemented")




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
