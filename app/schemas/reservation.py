from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class ReservationBase(BaseModel):
    """
    Base schema for reservation-related data.

    Attributes:
        restaurant_id (int): ID of the restaurant being reserved.
        user_id (int): ID of the user making the reservation.
        reservation_time (datetime): Date and time of the reservation.
        party_size (int): Number of people in the party.
        status (str): Current status of the reservation.
        special_requests (Optional[str]): Any special requests or notes.
    """
    restaurant_id: int = Field(..., example=1)
    user_id: int = Field(..., example=1)
    reservation_time: datetime = Field(..., example="2024-04-18T19:00:00Z")
    party_size: int = Field(..., example=4)
    status: str = Field("pending", example="confirmed")
    special_requests: Optional[str] = Field(None, example="Window seat preferred")
    table_number: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class ReservationCreate(ReservationBase):
    """
    Schema for creating a new reservation with validation rules.

    Attributes:
        restaurant_id (int): ID of the restaurant being reserved. Must be positive.
        user_id (int): ID of the user making the reservation. Must be positive.
        reservation_time (datetime): Date and time of the reservation. Must be in the future.
        party_size (int): Number of people in the party. Must be between 1 and 20.
        status (str): Initial status of the reservation. Must be one of: pending, confirmed, cancelled.
        special_requests (Optional[str]): Any special requests or notes. Max 500 characters.
        table_preference (Optional[str]): Preferred table type or location.
        table_number (Optional[int]): Specific table number requested. Must be positive.
        duration_minutes (Optional[int]): Expected duration of the reservation in minutes.
        contact_phone (Optional[str]): Contact phone number for the reservation.
        contact_email (Optional[str]): Contact email for the reservation.
        occasion (Optional[str]): Special occasion if any.
        dietary_restrictions (Optional[List[str]]): List of dietary restrictions.
    """
    restaurant_id: int = Field(
        ...,
        gt=0,
        description="ID of the restaurant being reserved",
        example=1
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user making the reservation",
        example=1
    )
    reservation_time: datetime = Field(
        ...,
        description="Date and time of the reservation",
        example="2024-04-18T19:00:00Z"
    )
    party_size: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of people in the party",
        example=4
    )
    status: str = Field(
        "pending",
        pattern="^(pending|confirmed|cancelled)$",
        description="Initial status of the reservation",
        example="pending"
    )
    special_requests: Optional[str] = Field(
        None,
        max_length=500,
        description="Any special requests or notes",
        example="Window seat preferred, celebrating anniversary"
    )
    table_preference: Optional[str] = Field(
        None,
        pattern="^(window|booth|bar|outdoor|private)$",
        description="Preferred table type or location",
        example="window"
    )
    table_number: Optional[int] = Field(
        None,
        gt=0,
        description="Specific table number requested",
        example=12
    )
    contact_phone: Optional[str] = Field(
        None,
        pattern="^\+?[1-9]\d{1,14}$",
        description="Contact phone number for the reservation",
        example="+1234567890"
    )
    contact_email: Optional[str] = Field(
        None,
        pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Contact email for the reservation",
        example="customer@example.com"
    )
    occasion: Optional[str] = Field(
        None,
        pattern="^(birthday|anniversary|business|other)$",
        description="Special occasion if any",
        example="anniversary"
    )

    model_config = ConfigDict(from_attributes=True)

class ReservationUpdate(ReservationBase):
    """
    Schema for updating an existing reservation.
    All fields are optional to allow partial updates.

    Attributes:
        reservation_time (Optional[datetime]): New date and time of the reservation. Must be in the future.
        party_size (Optional[int]): Updated number of people in the party. Must be between 1 and 20.
        status (Optional[str]): Updated status of the reservation. Must be one of: pending, confirmed, cancelled.
        special_requests (Optional[str]): Updated special requests or notes. Max 500 characters.
        table_preference (Optional[str]): Updated preferred table type or location.
        table_number (Optional[int]): Updated specific table number requested. Must be positive.
        duration_minutes (Optional[int]): Updated expected duration in minutes. Must be between 30 and 240.
        contact_phone (Optional[str]): Updated contact phone number.
        contact_email (Optional[str]): Updated contact email.
        occasion (Optional[str]): Updated special occasion.
        updated_by (str): Who is making the update (e.g., 'customer', 'restaurant', 'admin').
        update_reason (Optional[str]): Reason for the update. Required if status is changed to 'cancelled'.
    """
    reservation_time: Optional[datetime] = Field(
        None,
        description="New date and time of the reservation",
        example="2024-04-18T19:00:00Z"
    )
    party_size: Optional[int] = Field(
        None,
        ge=1,
        le=20,
        description="Updated number of people in the party",
        example=4
    )
    status: Optional[str] = Field(
        None,
        pattern="^(pending|confirmed|cancelled)$",
        description="Updated status of the reservation",
        example="confirmed"
    )
    special_requests: Optional[str] = Field(
        None,
        max_length=500,
        description="Updated special requests or notes",
        example="Window seat preferred, celebrating anniversary"
    )
    table_preference: Optional[str] = Field(
        None,
        pattern="^(window|booth|bar|outdoor|private)$",
        description="Updated preferred table type or location",
        example="window"
    )
    table_number: Optional[int] = Field(
        None,
        gt=0,
        description="Updated specific table number requested",
        example=12
    )
    contact_phone: Optional[str] = Field(
        None,
        pattern="^\+?[1-9]\d{1,14}$",
        description="Updated contact phone number",
        example="+1234567890"
    )
    contact_email: Optional[str] = Field(
        None,
        pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Updated contact email",
        example="customer@example.com"
    )
    occasion: Optional[str] = Field(
        None,
        pattern="^(birthday|anniversary|business|other)$",
        description="Updated special occasion",
        example="anniversary"
    )
    updated_by: str = Field(
        ...,
        pattern="^(customer|restaurant|admin)$",
        description="Who is making the update",
        example="customer"
    )
    update_reason: Optional[str] = Field(
        None,
        min_length=5,
        max_length=500,
        description="Reason for the update",
        example="Change in party size"
    )

    model_config = ConfigDict(from_attributes=True)

    def validate_cancellation(self) -> bool:
        """
        Validates that update_reason is provided when status is changed to 'cancelled'.
        
        Returns:
            bool: True if validation passes, False otherwise
        """
        if self.status == "cancelled" and not self.update_reason:
            return False
        return True

class ReservationRead(ReservationBase):
    """
    Schema for returning reservation data to the client.

    Inherits from ReservationBase and includes additional fields for reservation identification.

    Attributes:
        id (int): The unique identifier for the reservation.
        user_id (int): The ID of the user who made the reservation.
        restaurant_id (int): The ID of the restaurant for the reservation.
        status (str): The current status of the reservation (e.g., "confirmed", "cancelled").
        reservation_time (datetime): The date and time of the reservation.
        party_size (int): The number of people in the party.
        special_requests (Optional[str]): Any special requests or notes.
        table_number (Optional[int]): The specific table number assigned.
        created_at (datetime): The timestamp when the reservation was created.
        updated_at (Optional[datetime]): The timestamp when the reservation was last updated.
    """
    id: int = Field(
        ...,
        description="The unique identifier for the reservation",
        example=101
    )
    restaurant_id: int = Field(
        ...,
        description="The ID of the restaurant for the reservation",
        example=1
    )
    user_id: int = Field(
        ...,
        description="The ID of the user who made the reservation",
        example=1
    )
    status: str = Field(
        ...,
        description="The current status of the reservation",
        example="confirmed"
    )
    reservation_time: datetime = Field(
        ...,
        description="The date and time of the reservation",
        example="2024-04-18T19:00:00Z"
    )
    party_size: int = Field(
        ...,
        description="The number of people in the party",
        example=4
    )
    special_requests: Optional[str] = Field(
        None,
        description="Any special requests or notes",
        example="Window seat preferred"
    )
    table_number: Optional[int] = Field(
        None,
        description="The specific table number assigned",
        example=12
    )
    created_at: datetime = Field(
        ...,
        description="The timestamp when the reservation was created",
        example="2024-04-01T12:00:00Z"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="The timestamp when the reservation was last updated",
        example="2024-04-10T15:30:00Z"
    )

    model_config = ConfigDict(from_attributes=True)
