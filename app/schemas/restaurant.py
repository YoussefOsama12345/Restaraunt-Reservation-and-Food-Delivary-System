from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class RestaurantBase(BaseModel):
    """
    Base schema for restaurant-related data.

    Attributes:
        name (str): The name of the restaurant.
        address (str): The physical address of the restaurant.
        contact (Optional[str]): The contact number for the restaurant, if available.
        hours (Optional[str]): The operating hours of the restaurant (e.g., "9am - 11pm").
        is_active (Optional[bool]): Indicates whether the restaurant is currently active (default is True).
    """
    name: str
    address: str
    contact: Optional[str] = None
    hours: Optional[str] = Field(None, example="9am - 11pm")
    is_active: Optional[bool] = True

    model_config = ConfigDict(from_attributes=True)

class RestaurantCreate(RestaurantBase):
    """
    Schema for creating a new restaurant.

    Attributes:
        name (str): Name of the restaurant. Must be unique and between 2-100 characters.
        description (Optional[str]): Description or bio of the restaurant.
        location (str): Physical address or location of the restaurant.
        cuisine_type (Optional[str]): Type of cuisine offered (e.g., Italian, Indian).
        phone (Optional[str]): Contact phone number.
        opening_hours (Optional[str]): Operating hours of the restaurant.
        website (Optional[str]): Restaurant's website URL.
        capacity (Optional[int]): Total seating capacity.
        delivery_radius (Optional[float]): Maximum delivery radius in kilometers.
        minimum_order (Optional[float]): Minimum order amount for delivery.
    """
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Name of the restaurant",
        example="La Bella Italia"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Description or bio of the restaurant",
        example="Authentic Italian cuisine in a cozy atmosphere"
    )
    location: str = Field(
        ...,
        max_length=255,
        description="Physical address or location",
        example="123 Main Street, Cityville, ST 12345"
    )
    cuisine_type: Optional[str] = Field(
        None,
        max_length=100,
        description="Type of cuisine offered",
        example="Italian"
    )
    phone: Optional[str] = Field(
        None,
        pattern="^\+?[1-9]\d{1,14}$",
        description="Contact phone number",
        example="+1234567890"
    )
    opening_hours: Optional[str] = Field(
        None,
        max_length=200,
        description="Operating hours",
        example="Mon-Sat: 11:00-22:00, Sun: 12:00-21:00"
    )
    website: Optional[str] = Field(
        None,
        pattern="^https?://.*",
        description="Restaurant website URL",
        example="https://labellaitalia.com"
    )
    capacity: Optional[int] = Field(
        None,
        gt=0,
        description="Total seating capacity",
        example=80
    )
    delivery_radius: Optional[float] = Field(
        None,
        gt=0,
        description="Maximum delivery radius in kilometers",
        example=5.0
    )
    minimum_order: Optional[float] = Field(
        None,
        ge=0,
        description="Minimum order amount for delivery",
        example=15.0
    )

    model_config = ConfigDict(from_attributes=True)

class RestaurantUpdate(RestaurantBase):
    """
    Schema for updating an existing restaurant.
    All fields are optional to allow partial updates.

    Attributes:
        name (Optional[str]): Updated name of the restaurant. Must be between 2-100 characters.
        description (Optional[str]): Updated description or bio of the restaurant.
        location (Optional[str]): Updated physical address or location.
        cuisine_type (Optional[str]): Updated type of cuisine offered.
        phone (Optional[str]): Updated contact phone number.
        opening_hours (Optional[str]): Updated operating hours.
        website (Optional[str]): Updated restaurant website URL.
        capacity (Optional[int]): Updated total seating capacity.
        delivery_radius (Optional[float]): Updated maximum delivery radius in kilometers.
        minimum_order (Optional[float]): Updated minimum order amount for delivery.
        is_active (Optional[bool]): Updated active status of the restaurant.
        updated_by (str): Who is making the update (e.g., 'admin', 'manager').
        update_reason (Optional[str]): Reason for the update.
    """
    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Updated name of the restaurant",
        example="La Bella Italia"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Updated description or bio of the restaurant",
        example="Authentic Italian cuisine in a cozy atmosphere"
    )
    location: Optional[str] = Field(
        None,
        max_length=255,
        description="Updated physical address or location",
        example="123 Main Street, Cityville, ST 12345"
    )
    cuisine_type: Optional[str] = Field(
        None,
        max_length=100,
        description="Updated type of cuisine offered",
        example="Italian"
    )
    phone: Optional[str] = Field(
        None,
        pattern="^\+?[1-9]\d{1,14}$",
        description="Updated contact phone number",
        example="+1234567890"
    )
    opening_hours: Optional[str] = Field(
        None,
        max_length=200,
        description="Updated operating hours",
        example="Mon-Sat: 11:00-22:00, Sun: 12:00-21:00"
    )
    website: Optional[str] = Field(
        None,
        pattern="^https?://.*",
        description="Updated restaurant website URL",
        example="https://labellaitalia.com"
    )
    capacity: Optional[int] = Field(
        None,
        gt=0,
        description="Updated total seating capacity",
        example=80
    )
    delivery_radius: Optional[float] = Field(
        None,
        gt=0,
        description="Updated maximum delivery radius in kilometers",
        example=5.0
    )
    minimum_order: Optional[float] = Field(
        None,
        ge=0,
        description="Updated minimum order amount for delivery",
        example=15.0
    )
    is_active: Optional[bool] = Field(
        None,
        description="Updated active status of the restaurant",
        example=True
    )
    updated_by: str = Field(
        ...,
        pattern="^(admin|manager)$",
        description="Who is making the update",
        example="admin"
    )
    update_reason: Optional[str] = Field(
        None,
        max_length=500,
        description="Reason for the update",
        example="Updated contact information and operating hours"
    )

    model_config = ConfigDict(from_attributes=True)

class RestaurantRead(RestaurantBase):
    """
    Schema for returning restaurant data to the client.

    Attributes:
        id (int): The unique identifier for the restaurant.
        name (str): Name of the restaurant.
        description (Optional[str]): Description or bio of the restaurant.
        location (str): Physical address/location of the restaurant.
        cuisine_type (Optional[str]): Type of cuisine offered.
        phone (Optional[str]): Contact phone number.
        opening_hours (Optional[str]): Operating hours.
        website (Optional[str]): Restaurant website URL.
        capacity (Optional[int]): Total seating capacity.
        delivery_radius (Optional[float]): Maximum delivery radius in kilometers.
        minimum_order (Optional[float]): Minimum order amount for delivery.
        average_rating (Optional[float]): Average customer rating.
        total_reviews (Optional[int]): Total number of customer reviews.
        is_active (bool): Whether the restaurant is currently active.
        created_at (datetime): When the restaurant was created.
        updated_at (datetime): When the restaurant was last updated.
    """
    id: int = Field(
        ...,
        description="Unique identifier for the restaurant",
        example=1
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Description or bio of the restaurant",
        example="Authentic Italian cuisine in a cozy atmosphere"
    )
    cuisine_type: Optional[str] = Field(
        None,
        max_length=100,
        description="Type of cuisine offered",
        example="Italian"
    )
    website: Optional[str] = Field(
        None,
        pattern="^https?://.*",
        description="Restaurant website URL",
        example="https://labellaitalia.com"
    )
    capacity: Optional[int] = Field(
        None,
        gt=0,
        description="Total seating capacity",
        example=80
    )
    delivery_radius: Optional[float] = Field(
        None,
        gt=0,
        description="Maximum delivery radius in kilometers",
        example=5.0
    )
    minimum_order: Optional[float] = Field(
        None,
        ge=0,
        description="Minimum order amount for delivery",
        example=15.0
    )
    average_rating: Optional[float] = Field(
        None,
        ge=0.0,
        le=5.0,
        description="Average customer rating (0-5)",
        example=4.5
    )
    total_reviews: Optional[int] = Field(
        0,
        ge=0,
        description="Total number of customer reviews",
        example=42
    )
    created_at: datetime = Field(
        ...,
        description="When the restaurant was created",
        example="2024-04-18T10:00:00Z"
    )
    updated_at: datetime = Field(
        ...,
        description="When the restaurant was last updated",
        example="2024-04-18T15:30:00Z"
    )

    model_config = ConfigDict(from_attributes=True)
