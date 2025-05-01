"""
Cart schema definitions using Pydantic.

Defines models for creating, updating, and retrieving cart items for authenticated users.
Each cart item represents a menu item selected by the user and its desired quantity.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CartItemBase(BaseModel):
    """
    Shared base schema for cart item fields.
    """
    menu_item_id: int = Field(..., description="ID of the selected menu item")
    quantity: int = Field(..., gt=0, description="Quantity of the item in the cart")

    class Config:
        orm_mode = True


class CartItemCreate(CartItemBase):
    """
    Schema for adding a new item to the user's cart with validation rules.
    """
    special_instructions: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Special instructions for this item",
        example="No onions, extra spicy"
    )
    selected_options: Optional[List[int]] = Field(
        default=None,
        description="IDs of selected menu item options",
        example=[1, 3]
    )

    class Config:
        orm_mode = True


class CartItemUpdate(BaseModel):
    """
    Schema for updating the quantity of an item in the cart with validation rules.
    """
    quantity: int = Field(
        gt=0,
        description="New quantity for the cart item",
        example=3
    )
    special_instructions: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Updated special instructions for this item",
        example="Extra cheese, no tomatoes"
    )
    selected_options: Optional[List[int]] = Field(
        default=None,
        description="Updated list of selected menu item options",
        example=[2, 4]
    )

    class Config:
        orm_mode = True


class CartItemRead(CartItemBase):
    """
    Schema for reading cart item details from the system.
    """
    id: int = Field(description="Unique identifier of the cart item")
    user_id: int = Field(description="ID of the user who owns the cart")
    created_at: datetime = Field(description="When the item was added to the cart")
    updated_at: datetime = Field(description="When the item was last updated")
    menu_item_name: str = Field(description="Name of the menu item")
    menu_item_price: float = Field(gt=0, description="Current price of the menu item")
    special_instructions: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Special instructions for this item"
    )
    selected_options: Optional[List[int]] = Field(
        default=None,
        description="IDs of selected menu item options"
    )
    option_names: Optional[List[str]] = Field(
        default=None,
        description="Names of the selected options"
    )
    subtotal: float = Field(gt=0, description="Calculated subtotal for this item")

    class Config:
        orm_mode = True
