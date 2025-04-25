"""
Address schema definitions using Pydantic 2.9.2.

These models define the structure for creating, updating, and reading user address data,
including validation rules and example values for OpenAPI documentation.

Used for user address book management in delivery and billing flows.
"""
# ---
# UPDATED BY AI: Updated schema field names to match DB (street_address, postal_code), added orm_mode for from_orm, 
# improved validation, and ensured Pydantic v1/v2 compatibility for FastAPI response models.
# ---
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class AddressBase(BaseModel):
    """
    Shared base schema for address fields.
    """
    street_address: str = Field(example="123 Elm St")
    city: str = Field(example="New York")
    state: Optional[str] = Field(default=None, example="NY")
    country: str = Field(example="USA")
    postal_code: str = Field(example="10001")
    is_default: Optional[bool] = Field(default=False, description="Whether this is the user's default address")
    label: Optional[str] = Field(default=None, example="Home or Work")

    model_config = ConfigDict(from_attributes=True)


class AddressCreate(AddressBase):
    """
    Schema for creating a new address record with validation rules.
    """
    street_address: str = Field(
        min_length=5,
        max_length=100,
        description="Street name and number",
        example="123 Elm St"
    )
    city: str = Field(
        min_length=2,
        max_length=50,
        description="City name",
        example="New York"
    )
    state: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=2,
        description="State or province code",
        example="NY"
    )
    country: str = Field(
        min_length=2,
        max_length=50,
        description="Country name",
        example="USA"
    )
    postal_code: str = Field(
        min_length=3,
        max_length=10,
        description="Postal or ZIP code",
        example="10001"
    )
    is_default: Optional[bool] = Field(
        default=False,
        description="Whether this is the user's default address"
    )
    label: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=20,
        description="Optional label for address like 'Home' or 'Work'",
        example="Home"
    )

    model_config = ConfigDict(from_attributes=True)


class AddressUpdate(AddressBase):
    """
    Schema for updating an existing address record with validation rules.
    All fields are optional to allow partial updates.
    """
    street_address: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=100,
        description="Street name and number",
        example="123 Elm St"
    )
    city: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="City name",
        example="New York"
    )
    state: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=2,
        description="State or province code",
        example="NY"
    )
    country: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="Country name",
        example="USA"
    )
    postal_code: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=10,
        description="Postal or ZIP code",
        example="10001"
    )
    is_default: Optional[bool] = Field(
        default=None,
        description="Whether this is the user's default address"
    )
    label: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=20,
        description="Optional label for address like 'Home' or 'Work'",
        example="Home"
    )

    model_config = ConfigDict(from_attributes=True)


class AddressRead(AddressBase):
    """
    Schema for returning address data to the client.
    Inherits from AddressBase and includes additional fields for address identification.
    """
    id: int = Field(description="Unique identifier of the address")
    user_id: int = Field(description="ID of the user who owns this address")
    created_at: datetime = Field(description="When the address was created")
    updated_at: datetime = Field(description="When the address was last updated")
    is_active: bool = Field(default=True, description="Whether the address is currently active")
    last_used_at: Optional[datetime] = Field(default=None, description="When the address was last used for delivery")
    usage_count: int = Field(default=0, ge=0, description="Number of times this address has been used")

    class Config:
        orm_mode = True

    model_config = ConfigDict(from_attributes=True)
