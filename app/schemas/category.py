"""
Category schema definitions using Pydantic 2.9.2.

Defines request and response models for food menu categories.
Supports creation, updating, and returning category information.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class CategoryBase(BaseModel):
    """
    Base schema shared across creation and update models.
    """
    name: str = Field(
        max_length=100,
        example="Desserts"
    )
    description: str = Field(
        example="Sweet items served after main course."
    )

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(CategoryBase):
    """
    Schema for creating a new category with validation rules.
    """
    name: str = Field(
        min_length=2,
        max_length=100,
        description="Name of the category",
        example="Desserts"
    )
    description: str = Field(
        min_length=10,
        max_length=500,
        description="Description of the category",
        example="Sweet items served after main course, including cakes, pastries, and ice creams."
    )
    image_url: Optional[str] = Field(
        default=None,
        description="URL of the category image",
        example="https://example.com/images/desserts.jpg"
    )
    is_active: bool = Field(
        default=True,
        description="Whether the category is currently active"
    )
    display_order: int = Field(
        default=0,
        ge=0,
        description="Order in which the category should be displayed"
    )
    parent_id: Optional[int] = Field(
        default=None,
        ge=1,
        description="ID of the parent category if this is a subcategory"
    )

    model_config = ConfigDict(from_attributes=True)


class CategoryUpdate(BaseModel):
    """
    Schema for updating an existing category with validation rules.
    All fields are optional to allow partial updates.
    """
    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100,
        description="Updated name of the category",
        example="Desserts"
    )
    description: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=500,
        description="Updated description of the category",
        example="Sweet items served after main course, including cakes, pastries, and ice creams."
    )
    image_url: Optional[str] = Field(
        default=None,
        description="Updated URL of the category image",
        example="https://example.com/images/desserts.jpg"
    )
    is_active: Optional[bool] = Field(
        default=None,
        description="Updated active status of the category"
    )
    display_order: Optional[int] = Field(
        default=None,
        ge=0,
        description="Updated display order of the category"
    )
    parent_id: Optional[int] = Field(
        default=None,
        ge=1,
        description="Updated ID of the parent category"
    )

    model_config = ConfigDict(from_attributes=True)


class CategoryRead(CategoryBase):
    """
    Schema for returning category data to the client.
    """
    id: int = Field(description="Unique identifier of the category")
    created_at: datetime = Field(description="When the category was created")
    updated_at: datetime = Field(description="When the category was last updated")
    image_url: Optional[str] = Field(default=None, description="URL of the category image")
    is_active: bool = Field(default=True, description="Whether the category is currently active")
    display_order: int = Field(default=0, ge=0, description="Order in which the category should be displayed")
    parent_id: Optional[int] = Field(default=None, ge=1, description="ID of the parent category if this is a subcategory")
    parent_name: Optional[str] = Field(default=None, description="Name of the parent category if this is a subcategory")
    item_count: int = Field(default=0, ge=0, description="Number of menu items in this category")
    total_sales: float = Field(default=0.0, ge=0.0, description="Total sales from items in this category")
    average_rating: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=5.0,
        description="Average rating of items in this category"
    )

    model_config = ConfigDict(from_attributes=True)
