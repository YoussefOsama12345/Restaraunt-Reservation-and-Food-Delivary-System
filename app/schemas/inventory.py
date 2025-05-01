"""
Inventory schema definitions using Pydantic 2.0.

Defines models for creating, updating, and reading inventory items such as
ingredients, packaging materials, or stock-tracked assets.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class InventoryItemBase(BaseModel):
    """Shared fields for inventory item creation and updates."""
    item_name: str = Field(..., example="Tomatoes")
    quantity: int = Field(..., example=100)
    unit: str = Field(..., example="kg")
    reorder_level: int = Field(..., example=10, description="Minimum stock level before triggering low-stock alerts")
    category: Optional[str] = Field(None, example="ingredients")
    supplier_id: Optional[int] = Field(None, example=5)
    cost_per_unit: Optional[float] = Field(None, example=2.99)
    expiry_date: Optional[datetime] = Field(None)
    storage_location: Optional[str] = Field(None, example="Refrigerator A, Shelf 2")
    audit_notes: Optional[str] = Field(None, example="Keep refrigerated at 4°C")

    model_config = ConfigDict(from_attributes=True)


class InventoryItemCreate(InventoryItemBase):
    """Schema for creating a new inventory item with validation rules."""
    restaurant_id: int = Field(..., example=1)

    model_config = ConfigDict(from_attributes=True)


class InventoryItemUpdate(BaseModel):
    """Schema for updating an existing inventory item. Allows partial updates."""
    item_name: Optional[str] = Field(None, example="Tomatoes")
    quantity: Optional[int] = Field(None, example=100)
    unit: Optional[str] = Field(None, example="kg")
    reorder_level: Optional[int] = Field(None, example=10)
    category: Optional[str] = Field(None, example="ingredients")
    supplier_id: Optional[int] = Field(None, example=5)
    cost_per_unit: Optional[float] = Field(None, example=2.99)
    expiry_date: Optional[datetime] = Field(None)
    storage_location: Optional[str] = Field(None, example="Refrigerator A, Shelf 2")
    audit_notes: Optional[str] = Field(None, example="Keep refrigerated at 4°C")
    is_active: Optional[bool] = Field(None, example=True)
    last_restocked_at: Optional[datetime] = Field(None)
    last_used_at: Optional[datetime] = Field(None)
    days_until_restock: Optional[int] = Field(None, example=7)
    days_until_expiry: Optional[int] = Field(None, example=30)

    model_config = ConfigDict(from_attributes=True)


class InventoryItemRead(InventoryItemBase):
    """Schema for returning inventory item data to clients."""
    id: int = Field(..., example=101)
    restaurant_id: int = Field(..., example=1)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    total_restocks: int = Field(..., example=5)
    total_usage: int = Field(..., example=500)
    average_usage_per_day: float = Field(..., example=2.5)
    low_stock_warning: bool = Field(..., example=False)
    last_audit_date: Optional[datetime] = Field(None)
    is_active: Optional[bool] = Field(True, example=True)
    last_restocked_at: Optional[datetime] = Field(None)
    last_used_at: Optional[datetime] = Field(None)
    days_until_restock: Optional[int] = Field(None, example=7)
    days_until_expiry: Optional[int] = Field(None, example=30)

    model_config = ConfigDict(from_attributes=True)
