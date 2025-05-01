"""
Delivery schema definitions using Pydantic v1.

Defines models for creating, updating, and reading delivery tasks,
including assignment to drivers, status tracking, and OTP confirmation.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# === BASE SCHEMA ===

class DeliveryBase(BaseModel):
    """
    Shared fields for delivery creation and updates.
    """
    order_id: int = Field(..., example=101)
    driver_id: int = Field(..., example=5)
    status: Optional[str] = Field("assigned", example="assigned")
    otp: Optional[str] = Field(None, example="845692")

    class Config:
        orm_mode = True


# === CREATE SCHEMA ===

class DeliveryCreate(DeliveryBase):
    """
    Schema for creating a new delivery task with validation.
    """
    order_id: int = Field(..., gt=0, example=101)
    driver_id: int = Field(..., gt=0, example=5)
    status: Optional[str] = Field(
        "assigned",
        pattern="^(assigned|en_route|delivered|cancelled)$",
        example="assigned"
    )
    otp: Optional[str] = Field(
        None,
        pattern="^[0-9]{6}$",
        example="845692"
    )
    estimated_delivery_time: Optional[datetime] = Field(None)
    delivery_instructions: Optional[str] = Field(None, max_length=500, example="Call before arrival")
    vehicle_type: Optional[str] = Field(
        None,
        pattern="^(bike|car|scooter|walk)$",
        example="bike"
    )
    priority_level: Optional[str] = Field(
        None,
        pattern="^(low|medium|high|urgent)$",
        example="medium"
    )

    class Config:
        orm_mode = True


# === STATUS UPDATE SCHEMA ===

class DeliveryUpdateStatus(BaseModel):
    """
    Schema for updating the status of a delivery.
    """
    status: str = Field(
        ...,
        pattern="^(assigned|en_route|arrived|delivered|cancelled)$",
        example="en_route"
    )
    status_notes: Optional[str] = Field(None, max_length=500, example="Traffic delay on main road")
    location_latitude: Optional[float] = Field(None, ge=-90, le=90, example=40.7128)
    location_longitude: Optional[float] = Field(None, ge=-180, le=180, example=-74.0060)
    estimated_time_remaining: Optional[int] = Field(None, ge=0, example=15)

    class Config:
        orm_mode = True


# === OTP CONFIRMATION SCHEMA ===

class DeliveryConfirm(BaseModel):
    """
    Schema for confirming a delivery via OTP.
    """
    otp: str = Field(
        ...,
        pattern="^[0-9]{6}$",
        example="123456"
    )
    delivery_id: int = Field(..., gt=0, example=101)
    driver_id: int = Field(..., gt=0, example=5)
    customer_signature: Optional[str] = Field(None, example="data:image/png;base64,iVBOR...")
    delivery_photo: Optional[str] = Field(None, example="data:image/jpeg;base64,/9j/4AA...")
    notes: Optional[str] = Field(None, max_length=500, example="Leave package at the front door")

    class Config:
        orm_mode = True


# === READ SCHEMA ===

class DeliveryRead(DeliveryBase):
    """
    Schema for reading delivery task details.
    """
    id: int = Field(..., gt=0, example=101)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    completed_at: Optional[datetime] = Field(None)
    customer_id: int = Field(..., gt=0, example=42)
    restaurant_id: int = Field(..., gt=0, example=15)
    delivery_address: str = Field(..., example="123 Main St, New York, NY 10001")
    estimated_delivery_time: Optional[datetime] = Field(None)
    actual_delivery_time: Optional[datetime] = Field(None)
    delivery_instructions: Optional[str] = Field(None, max_length=500)
    vehicle_type: Optional[str] = Field(None, pattern="^(bike|car|scooter|walk)$", example="bike")
    priority_level: Optional[str] = Field(None, pattern="^(low|medium|high|urgent)$", example="medium")
    distance_km: Optional[float] = Field(None, ge=0, example=5.2)
    delivery_fee: float = Field(..., ge=0, example=4.99)
    rating: Optional[int] = Field(None, ge=1, le=5, example=5)
    feedback: Optional[str] = Field(None, max_length=1000, example="Driver was punctual and professional")

    class Config:
        orm_mode = True
