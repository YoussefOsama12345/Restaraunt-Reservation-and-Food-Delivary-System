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
    name: str = Field(..., example="Tomatoes")
    quantity: int = Field(..., example=100)
    unit: str = Field(..., example="kg")
    threshold: Optional[int] = Field(10, example=10, description="Minimum stock level before triggering low-stock alerts")

    model_config = ConfigDict(from_attributes=True)


class InventoryItemCreate(InventoryItemBase):
    """Schema for creating a new inventory item with validation rules."""
    name: str = Field(..., min_length=2, max_length=100, example="Fresh Tomatoes")
    quantity: int = Field(..., ge=0, example=100)
    unit: str = Field(..., pattern="^(kg|g|l|ml|pieces|boxes|packs)$", example="kg")
    threshold: Optional[int] = Field(10, ge=0, example=10)
    category: Optional[str] = Field(None, pattern="^(ingredients|packaging|utensils|cleaning|other)$", example="ingredients")
    supplier_id: Optional[int] = Field(None, gt=0, example=5)
    cost_per_unit: Optional[float] = Field(None, gt=0, example=2.99)
    expiry_date: Optional[datetime] = Field(None)
    storage_location: Optional[str] = Field(None, max_length=100, example="Refrigerator A, Shelf 2")
    notes: Optional[str] = Field(None, max_length=500, example="Keep refrigerated at 4°C")

    model_config = ConfigDict(from_attributes=True)


class InventoryItemUpdate(InventoryItemBase):
    """Schema for updating an existing inventory item. Allows partial updates."""
    name: Optional[str] = Field(None, min_length=2, max_length=100, example="Fresh Tomatoes")
    quantity: Optional[int] = Field(None, ge=0, example=100)
    unit: Optional[str] = Field(None, pattern="^(kg|g|l|ml|pieces|boxes|packs)$", example="kg")
    threshold: Optional[int] = Field(None, ge=0, example=10)
    category: Optional[str] = Field(None, pattern="^(ingredients|packaging|utensils|cleaning|other)$", example="ingredients")
    supplier_id: Optional[int] = Field(None, gt=0, example=5)
    cost_per_unit: Optional[float] = Field(None, gt=0, example=2.99)
    expiry_date: Optional[datetime] = Field(None)
    storage_location: Optional[str] = Field(None, max_length=100, example="Refrigerator A, Shelf 2")
    notes: Optional[str] = Field(None, max_length=500, example="Keep refrigerated at 4°C")
    is_active: Optional[bool] = Field(None, example=True)
    last_restocked_at: Optional[datetime] = Field(None)
    last_used_at: Optional[datetime] = Field(None)

    model_config = ConfigDict(from_attributes=True)


class InventoryItemRead(InventoryItemBase):
    """Schema for returning inventory item data to clients."""
    id: int = Field(..., gt=0, example=101)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    category: str = Field(..., pattern="^(ingredients|packaging|utensils|cleaning|other)$", example="ingredients")
    supplier_id: Optional[int] = Field(None, gt=0, example=5)
    cost_per_unit: Optional[float] = Field(None, gt=0, example=2.99)
    expiry_date: Optional[datetime] = Field(None)
    storage_location: Optional[str] = Field(None, max_length=100, example="Refrigerator A, Shelf 2")
    notes: Optional[str] = Field(None, max_length=500, example="Keep refrigerated at 4°C")
    is_active: bool = Field(True, example=True)
    last_restocked_at: Optional[datetime] = Field(None)
    last_used_at: Optional[datetime] = Field(None)
    total_restocks: int = Field(0, ge=0, example=5)
    total_usage: int = Field(0, ge=0, example=500)
    average_usage_per_day: float = Field(0.0, ge=0.0, example=2.5)
    days_until_restock: Optional[int] = Field(None, ge=0, example=7)
    days_until_expiry: Optional[int] = Field(None, ge=0, example=30)
    low_stock_warning: bool = Field(False, example=False)
    last_audit_date: Optional[datetime] = Field(None)
    audit_notes: Optional[str] = Field(None, max_length=500, example="Quantity matches records")

    model_config = ConfigDict(from_attributes=True)
