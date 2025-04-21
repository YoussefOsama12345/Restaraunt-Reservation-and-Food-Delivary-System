from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserBase(BaseModel):
    """
    Base schema for user-related data.

    Attributes:
        username (str): The unique username of the user.
        email (EmailStr): The email address of the user.
        full_name (Optional[str]): The full name of the user.
        phone_number (Optional[str]): The contact number of the user.
        is_active (Optional[bool]): Indicates whether the user's account is active (default is True).
        is_admin (Optional[bool]): Indicates whether the user has admin privileges (default is False).
    """
    username: str = Field(..., example="john_doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    full_name: Optional[str] = Field(None, example="John Doe")
    phone_number: Optional[str] = Field(None, example="+1234567890")
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    """
    Schema for creating a new user.

    Attributes:
        username (str): Unique username for the account
        email (EmailStr): Valid email address
        password (str): Secure password for the account
        full_name (Optional[str]): User's full name
        phone_number (Optional[str]): Contact phone number
        is_active (Optional[bool]): Account activation status
        is_admin (Optional[bool]): Administrative privileges flag
    """
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",
        description="Unique username for the account",
        example="john_doe"
    )
    email: EmailStr = Field(
        ...,
        description="Valid email address for the account",
        example="john.doe@example.com"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="Secure password for the account",
        example="SecurePass123!"
    )
    full_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="User's full name",
        example="John Doe"
    )
    phone_number: Optional[str] = Field(
        None,
        pattern="^\+?[1-9][0-9]{7,14}$",
        description="International format phone number",
        example="+1234567890"
    )
    is_active: Optional[bool] = Field(
        True,
        description="Whether the user account is active",
        example=True
    )
    is_admin: Optional[bool] = Field(
        False,
        description="Whether the user has administrative privileges",
        example=False
    )

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(UserBase):
    """
    Schema for updating an existing user.
    All fields are optional to allow partial updates.

    Attributes:
        username (Optional[str]): Updated username
        email (Optional[EmailStr]): Updated email address
        full_name (Optional[str]): Updated full name
        phone_number (Optional[str]): Updated phone number
        is_active (Optional[bool]): Updated account status
        is_admin (Optional[bool]): Updated admin privileges
        password (Optional[str]): New password if changing
        update_reason (Optional[str]): Reason for the update
    """
    username: Optional[str] = Field(
        None,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",
        description="Updated username for the account",
        example="john_doe_new"
    )
    email: Optional[EmailStr] = Field(
        None,
        description="Updated email address",
        example="john.new@example.com"
    )
    full_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Updated full name",
        example="John M. Doe"
    )
    phone_number: Optional[str] = Field(
        None,
        pattern="^\+?[1-9][0-9]{7,14}$",
        description="Updated phone number in international format",
        example="+1987654321"
    )
    password: Optional[str] = Field(
        None,
        min_length=8,
        max_length=100,
        description="New password if being changed",
        example="NewSecurePass123!"
    )
    is_active: Optional[bool] = Field(
        None,
        description="Updated account activation status",
        example=True
    )
    is_admin: Optional[bool] = Field(
        None,
        description="Updated administrative privileges",
        example=False
    )
    
    model_config = ConfigDict(from_attributes=True)

class UserRead(UserBase):
    """
    Schema for returning user data to the client.

    Inherits from UserBase and includes additional fields for user identification.

    Attributes:
        id (int): Unique identifier for the user
        username (str): User's unique username
        email (EmailStr): User's email address
        full_name (Optional[str]): User's full name
        phone_number (Optional[str]): User's contact number
        is_active (bool): Account activation status
        is_admin (bool): Administrative privileges status
        created_at (datetime): When the account was created
        updated_at (Optional[datetime]): Last profile update timestamp
        last_login (Optional[datetime]): Last login timestamp
        orders_count (Optional[int]): Total number of orders
        reservations_count (Optional[int]): Total number of reservations
        total_spent (Optional[float]): Total amount spent on orders
        average_rating (Optional[float]): Average rating given to orders
        account_status (Optional[str]): Detailed account status
        verification_status (Optional[str]): Email/Phone verification status
    """
    id: int = Field(
        ...,
        gt=0,
        description="Unique identifier for the user",
        example=1
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",
        description="User's unique username",
        example="john_doe"
    )
    email: EmailStr = Field(
        ...,
        description="User's email address",
        example="john.doe@example.com"
    )
    full_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="User's full name",
        example="John Michael Doe"
    )
    phone_number: Optional[str] = Field(
        None,
        pattern="^\+?[1-9][0-9]{7,14}$",
        description="User's contact number in international format",
        example="+1234567890"
    )
    is_active: bool = Field(
        True,
        description="Whether the user account is currently active",
        example=True
    )
    is_admin: bool = Field(
        False,
        description="Whether the user has administrative privileges",
        example=False
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the account was created",
        example="2024-01-01T00:00:00Z"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp of last profile update",
        example="2024-04-18T15:30:00Z"
    )
    last_login: Optional[datetime] = Field(
        None,
        description="Timestamp of the last login",
        example="2024-04-18T15:30:00Z"
    )
    orders_count: Optional[int] = Field(
        0,
        ge=0,
        description="Total number of orders made by the user",
        example=5
    )
    reservations_count: Optional[int] = Field(
        0,
        ge=0,
        description="Total number of reservations made by the user",
        example=3
    )
    total_spent: Optional[float] = Field(
        0.0,
        ge=0.0,
        description="Total amount spent on orders",
        example=250.50
    )
    average_rating: Optional[float] = Field(
        None,
        ge=0.0,
        le=5.0,
        description="Average rating given to orders",
        example=4.5
    )
    account_status: Optional[str] = Field(
        "active",
        pattern="^(active|suspended|inactive|pending)$",
        description="Detailed account status",
        example="active"
    )
    verification_status: Optional[str] = Field(
        "unverified",
        pattern="^(unverified|email_verified|fully_verified)$",
        description="Email/Phone verification status",
        example="email_verified"
    )

    model_config = ConfigDict(from_attributes=True)
