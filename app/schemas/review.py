from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class ReviewBase(BaseModel):
    """
    Base schema for review-related data.

    Attributes:
        menu_item_id (int): The ID of the menu item being reviewed.
        restaurant_id (Optional[int]): The ID of the restaurant being reviewed, if applicable.
        user_id (int): The ID of the user who submitted the review.
        rating (float): The rating given by the user (typically between 1 and 5).
        comment (Optional[str]): An optional comment provided by the user about the menu item or restaurant.
        created_at (datetime): The timestamp when the review was created.
    """
    menu_item_id: int
    restaurant_id: Optional[int] = None
    user_id: int
    rating: float = Field(..., ge=1, le=5, example=5)  # Rating must be between 1 and 5
    comment: Optional[str] = Field(None, example="Great taste!")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class ReviewCreate(ReviewBase):
    """
    Schema for creating a new review.

    Inherits from ReviewBase and is used to validate data when creating a new review.
    
    Attributes:
        menu_item_id (int): The ID of the menu item being reviewed.
        restaurant_id (Optional[int]): The ID of the restaurant being reviewed.
        user_id (int): The ID of the user submitting the review.
        rating (float): Rating given by the user (1-5 stars).
        comment (Optional[str]): User's comments about the menu item.
        created_at (datetime): When the review was created (auto-generated).
    """
    menu_item_id: int = Field(
        ...,
        gt=0,
        description="ID of the menu item being reviewed",
        example=42
    )
    restaurant_id: Optional[int] = Field(
        None,
        gt=0,
        description="ID of the restaurant being reviewed (optional)",
        example=7
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user submitting the review",
        example=123
    )
    rating: float = Field(
        ...,
        ge=1.0,
        le=5.0,
        description="Rating from 1-5 stars (can include half-stars)",
        example=4.5
    )
    comment: Optional[str] = Field(
        None,
        min_length=2,
        max_length=500,
        description="User's comments about the menu item",
        example="Perfectly cooked and beautifully presented. Great flavors!"
    )

    model_config = ConfigDict(from_attributes=True,)

class ReviewUpdate(ReviewBase):
    """
    Schema for updating an existing review.
    All fields are optional to allow partial updates.

    Attributes:
        menu_item_id (Optional[int]): Updated ID of the menu item being reviewed.
        restaurant_id (Optional[int]): Updated ID of the restaurant being reviewed.
        rating (Optional[float]): Updated rating given by the user (1-5 stars).
        comment (Optional[str]): Updated user's comments about the menu item.
        updated_at (datetime): When the review was last updated (auto-generated).
        update_reason (Optional[str]): Reason for updating the review.
    """
    menu_item_id: Optional[int] = Field(
        None,
        gt=0,
        description="Updated ID of the menu item being reviewed",
        example=42
    )
    restaurant_id: Optional[int] = Field(
        None,
        gt=0,
        description="Updated ID of the restaurant being reviewed",
        example=7
    )
    user_id: Optional[int] = Field(
        None,
        gt=0,
        description="Updated ID of the user who submitted the review",
        example=123
    )
    rating: Optional[float] = Field(
        None,
        ge=1.0,
        le=5.0,
        description="Updated rating from 1-5 stars (can include half-stars)",
        example=4.0
    )
    comment: Optional[str] = Field(
        None,
        min_length=2,
        max_length=500,
        description="Updated user's comments about the menu item",
        example="Upon second visit, I still enjoyed the dish but found it slightly oversalted."
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When the review was last updated",
        example="2024-04-18T15:30:00Z"
    )
    update_reason: Optional[str] = Field(
        None,
        max_length=200,
        description="Reason for updating the review",
        example="Second visit to restaurant"
    )

    model_config = ConfigDict(from_attributes=True,)

class ReviewRead(ReviewBase):
    """
    Schema for returning review data to the client.

    Inherits from ReviewBase and includes additional fields for review identification.

    Attributes:
        id (int): The unique identifier for the review.
        menu_item_id (int): The ID of the menu item being reviewed.
        restaurant_id (Optional[int]): The ID of the restaurant being reviewed.
        user_id (int): The ID of the user who submitted the review.
        rating (float): Rating given by the user (1-5 stars).
        comment (Optional[str]): User's comments about the menu item.
        created_at (datetime): When the review was created.
        updated_at (Optional[datetime]): When the review was last updated, if applicable.
        menu_item_name (Optional[str]): Name of the menu item being reviewed.
        restaurant_name (Optional[str]): Name of the restaurant being reviewed.
        user_name (Optional[str]): Name of the user who submitted the review.        
        is_verified (bool): Whether this is a verified purchase review.
        helpful_votes (int): Number of users who found this review helpful.
    """
    id: int = Field(
        ...,
        description="Unique identifier for the review",
        example=1
    )
    menu_item_id: int = Field(
        ...,
        description="ID of the menu item being reviewed",
        example=42
    )
    restaurant_id: Optional[int] = Field(
        None,
        description="ID of the restaurant being reviewed",
        example=7
    )
    user_id: int = Field(
        ...,
        description="ID of the user who submitted the review",
        example=123
    )
    rating: float = Field(
        ...,
        ge=1.0,
        le=5.0,
        description="Rating from 1-5 stars",
        example=4.5
    )
    comment: Optional[str] = Field(
        None,
        description="User's comments about the menu item",
        example="Perfectly cooked and beautifully presented. Great flavors!"
    )
    created_at: datetime = Field(
        ...,
        description="When the review was created",
        example="2024-04-18T10:00:00Z"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="When the review was last updated, if applicable",
        example="2024-04-18T15:30:00Z"
    )
    menu_item_name: Optional[str] = Field(
        None,
        description="Name of the menu item being reviewed",
        example="Spaghetti Carbonara"
    )
    restaurant_name: Optional[str] = Field(
        None,
        description="Name of the restaurant being reviewed",
        example="La Bella Italia"
    )
    user_name: Optional[str] = Field(
        None,
        description="Name of the user who submitted the review",
        example="John Doe"
    )
    is_verified: bool = Field(
        default=False,
        description="Whether this is a verified purchase review",
        example=True
    )
    helpful_votes: Optional[int] = Field(
        default=0,
        ge=0,
        description="Number of users who found this review helpful",
        example=15
    )

    model_config = ConfigDict(from_attributes=True,)
