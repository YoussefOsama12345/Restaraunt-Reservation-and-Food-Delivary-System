"""
User Registration Service

Provides a completely synchronous implementation for user registration
to avoid any SQLAlchemy async/sync mixing issues.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from app.db.models.user import User, UserRole
from app.schemas.user import UserCreate
from app.settings import DATABASE_URL

# Create a synchronous password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create a synchronous engine and session
# Convert async URL to sync URL by removing the +asyncmy part
sync_database_url = DATABASE_URL.replace('+asyncmy', '')
sync_engine = create_engine(sync_database_url, echo=False)
SyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


def get_password_hash(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    """
    return pwd_context.hash(password)


def create_user(user_data: UserCreate) -> dict:
    """
    Create a new user with the given data.
    This is a completely synchronous implementation to avoid any async/sync mixing issues.
    
    Args:
        user_data: The user data to create a new user with
        
    Returns:
        A dictionary with the created user's data
        
    Raises:
        HTTPException: If the user creation fails
    """
    # Create a new synchronous session
    db = SyncSessionLocal()
    
    try:
        # Get role from user_data
        role_value = user_data.role.value if hasattr(user_data.role, 'value') else user_data.role
        
        # Map the role string to the model's UserRole enum
        if role_value == "admin":
            role = UserRole.ADMIN
        elif role_value == "driver":
            role = UserRole.DRIVER
        else:
            role = UserRole.CUSTOMER
        
        # Create the user
        user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
            full_name=user_data.full_name,
            phone_number=user_data.phone_number,
            is_active=True,
            role=role,
            account_status="active",
            verification_status="unverified"
        )
        
        # Add and commit
        db.add(user)
        db.commit()
        db.refresh(user)
        
        # Convert to dict
        user_dict = {c.name: getattr(user, c.name) for c in user.__table__.columns}
        return user_dict
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or username already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"User registration failed: {str(e)}")
    finally:
        db.close()
