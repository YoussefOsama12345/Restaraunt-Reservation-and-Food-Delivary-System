"""
MenuItem schema definitions using Pydantic 2.0.

Defines models for menu item creation, update, and response including
name, price, category, image, availability, and dietary flags.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class MenuItemBase(BaseModel):
    """Shared fields for menu item creation and updates."""
    name: str = Field(..., example="Margherita Pizza")
    description: Optional[str] = Field(None, example="Classic pizza with tomato, mozzarella, and basil.")
    price: float = Field(..., example=9.99)
    image_url: Optional[str] = Field(None, example="https://example.com/images/pizza.jpg")
    available: Optional[bool] = Field(True)
    is_vegetarian: Optional[bool] = Field(False)
    category_id: Optional[int] = Field(None, description="ID of the category this item belongs to")

    class Config:
        orm_mode = True


class MenuItemCreate(MenuItemBase):
    """Schema for creating a new menu item with validation rules."""
    name: str = Field(..., min_length=2, max_length=100, example="Margherita Pizza")
    description: Optional[str] = Field(
        None, min_length=10, max_length=500,
        example="Classic pizza with tomato sauce, fresh mozzarella, and basil"
    )
    price: float = Field(..., gt=0, example=9.99)
    image_url: Optional[str] = Field(
        None, pattern="^https?://.*", example="https://example.com/images/pizza.jpg"
    )
    available: bool = Field(True, example=True)
    is_vegetarian: bool = Field(False, example=True)
    category_id: int = Field(..., gt=0, example=1)
    restaurant_id: int = Field(..., gt=0, example=1)
    preparation_time: Optional[int] = Field(None, ge=0, example=15)
    calories: Optional[int] = Field(None, ge=0, example=850)
    ingredients: Optional[str] = Field(
        None, max_length=500, example="Tomato sauce, mozzarella cheese, fresh basil, olive oil"
    )
    tags: Optional[List[str]] = Field(
        None, max_items=10, example=["vegetarian", "italian", "pizza"]
    )

    class Config:
        orm_mode = True


class MenuItemUpdate(MenuItemBase):
    """Schema for updating an existing menu item with validation rules."""
    name: Optional[str] = Field(None, min_length=2, max_length=100, example="Margherita Pizza")
    description: Optional[str] = Field(
        None, min_length=10, max_length=500,
        example="Classic pizza with tomato sauce, fresh mozzarella, and basil"
    )
    price: Optional[float] = Field(None, gt=0, example=9.99)
    image_url: Optional[str] = Field(
        None, pattern="^https?://.*", example="https://example.com/images/pizza.jpg"
    )
    available: Optional[bool] = Field(None, example=True)
    is_vegetarian: Optional[bool] = Field(None, example=True)
    category_id: Optional[int] = Field(None, gt=0, example=1)
    preparation_time: Optional[int] = Field(None, ge=0, example=15)
    calories: Optional[int] = Field(None, ge=0, example=850)
    ingredients: Optional[str] = Field(
        None, max_length=500, example="Tomato sauce, mozzarella cheese, fresh basil, olive oil"
    )
    tags: Optional[List[str]] = Field(
        None, max_items=10, example=["vegetarian", "italian", "pizza"]
    )
    last_updated_by: Optional[str] = Field(None, min_length=3, max_length=50, example="chef_john")
    update_reason: Optional[str] = Field(None, max_length=200, example="Seasonal price adjustment")

    class Config:
        orm_mode = True


class MenuItemRead(MenuItemBase):
    """Schema for returning menu item data to clients."""
    id: int = Field(..., gt=0, example=101)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    category_name: str = Field(..., example="Pizza")
    preparation_time: int = Field(..., ge=0, example=15)
    calories: int = Field(..., ge=0, example=850)
    ingredients: str = Field(..., max_length=500, example="Tomato sauce, mozzarella cheese, fresh basil, olive oil")
    tags: List[str] = Field(..., max_items=10, example=["vegetarian", "italian", "pizza"])
    last_ordered_at: Optional[datetime] = Field(None)
    nutritional_info: Optional[dict] = Field(
        None,
        example={"protein": "20g", "carbs": "45g", "fat": "15g", "fiber": "3g"}
    )
    cooking_instructions: Optional[str] = Field(
        None,
        max_length=1000,
        example="Preheat oven to 450°F. Spread sauce, add toppings, bake for 12-15 minutes."
    )
    serving_size: Optional[str] = Field(None, example="1 pizza (12 inches)")
    estimated_cooking_time: Optional[int] = Field(None, ge=0, example=15)
    average_rating: float = Field(0.0, ge=0.0, le=5.0, example=4.5)
    total_orders: int = Field(0, ge=0, example=150)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
