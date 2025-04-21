from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


class NotificationBase(BaseModel):
    """
    Shared fields for notifications.

    Attributes:
        message (str): Main notification text.
        type (str): Notification category (e.g., 'order', 'reservation').
        is_read (bool): Whether the notification has been read.
    """
    message: str = Field(..., example="Your order #1234 has been shipped.")
    type: Optional[str] = Field(default="general", example="order")
    is_read: Optional[bool] = Field(default=False, description="True if the user has viewed the notification")

    model_config = ConfigDict(from_attributes=True)


class NotificationCreate(NotificationBase):
    """
    Schema for creating a new notification with validation rules.

    Attributes:
        user_id (int): ID of the user receiving the notification. Must be positive.
        message (str): Main notification text. Must be between 5 and 500 characters.
        type (str): Notification category. Must be one of: order, reservation, payment, delivery, system, general.
        priority (Optional[str]): Priority level of the notification. Must be one of: low, medium, high, urgent.
        action_url (Optional[str]): URL for any action associated with the notification.
        metadata (Optional[dict]): Additional data related to the notification.
        expires_at (Optional[datetime]): When the notification should expire.
        tags (Optional[List[str]]): List of tags for categorizing the notification.
    """
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user receiving the notification",
        example=1
    )
    message: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Main notification text",
        example="Your order #1234 has been shipped and will arrive in 30 minutes."
    )
    type: str = Field(
        "general",
        pattern="^(order|reservation|payment|delivery|system|general)$",
        description="Category of the notification",
        example="order"
    )
    priority: Optional[str] = Field(
        "medium",
        pattern="^(low|medium|high|urgent)$",
        description="Priority level of the notification",
        example="high"
    )
    action_url: Optional[str] = Field(
        None,
        pattern="^https?://.*",
        description="URL for any action associated with the notification",
        example="https://example.com/orders/1234"
    )
    metadata: Optional[dict] = Field(
        None,
        description="Additional data related to the notification",
        example={
            "order_id": 1234,
            "delivery_time": "30 minutes",
            "tracking_number": "TRK123456"
        }
    )
    expires_at: Optional[datetime] = Field(
        None,
        description="When the notification should expire",
        example="2024-04-19T12:00:00Z"
    )
    tags: Optional[List[str]] = Field(
        None,
        max_items=5,
        description="List of tags for categorizing the notification",
        example=["order_update", "delivery", "urgent"]
    )

    model_config = ConfigDict(from_attributes=True)


class NotificationUpdate(BaseModel):
    """
    Schema for updating notification status with validation rules.

    Attributes:
        is_read (bool): Whether the notification has been read or not.
        read_at (Optional[datetime]): When the notification was read.
        archived (Optional[bool]): Whether the notification has been archived.
        archived_at (Optional[datetime]): When the notification was archived.
        priority (Optional[str]): Updated priority level. Must be one of: low, medium, high, urgent.
        action_taken (Optional[bool]): Whether action has been taken on the notification.
        action_taken_at (Optional[datetime]): When action was taken.
        action_notes (Optional[str]): Notes about the action taken.
    """
    is_read: bool = Field(
        ...,
        description="Whether the notification has been read",
        example=True
    )
    read_at: Optional[datetime] = Field(
        None,
        description="When the notification was read",
        example="2024-04-18T15:30:00Z"
    )
    archived: Optional[bool] = Field(
        None,
        description="Whether the notification has been archived",
        example=False
    )
    archived_at: Optional[datetime] = Field(
        None,
        description="When the notification was archived",
        example="2024-04-18T16:00:00Z"
    )
    priority: Optional[str] = Field(
        None,
        pattern="^(low|medium|high|urgent)$",
        description="Updated priority level of the notification",
        example="medium"
    )
    action_taken: Optional[bool] = Field(
        None,
        description="Whether action has been taken on the notification",
        example=True
    )
    action_taken_at: Optional[datetime] = Field(
        None,
        description="When action was taken",
        example="2024-04-18T15:45:00Z"
    )
    action_notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Notes about the action taken",
        example="Customer confirmed receipt of order"
    )

    model_config = ConfigDict(from_attributes=True)


class NotificationRead(NotificationBase):
    """
    Schema for reading notifications from the database.

    Attributes:
        id (int): Unique identifier of the notification.
        user_id (int): ID of the user who received the notification.
        created_at (datetime): When the notification was created.
        read_at (Optional[datetime]): When the notification was read.
        archived (bool): Whether the notification has been archived.
        archived_at (Optional[datetime]): When the notification was archived.
        priority (str): Priority level of the notification.
        action_taken (bool): Whether action has been taken on the notification.
        action_taken_at (Optional[datetime]): When action was taken.
        action_notes (Optional[str]): Notes about the action taken.
        expires_at (Optional[datetime]): When the notification expires.
        tags (List[str]): List of tags for the notification.
        metadata (dict): Additional data related to the notification.
    """
    id: int = Field(
        ...,
        gt=0,
        description="Unique identifier of the notification",
        example=1
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user who received the notification",
        example=42
    )
    created_at: datetime = Field(
        ...,
        description="When the notification was created",
        example="2024-04-18T15:00:00Z"
    )
    read_at: Optional[datetime] = Field(
        None,
        description="When the notification was read",
        example="2024-04-18T15:30:00Z"
    )
    archived: Optional[bool] = Field(
        False,
        description="Whether the notification has been archived",
        example=False
    )
    archived_at: Optional[datetime] = Field(
        None,
        description="When the notification was archived",
        example="2024-04-18T16:00:00Z"
    )
    action_notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Notes about the action taken",
        example="Customer confirmed receipt of order"
    )
    tags: List[str] = Field(
        ...,
        max_items=5,
        description="List of tags for the notification",
        example=["order_update", "delivery", "urgent"]
    )
    metadata: dict = Field(
        ...,
        description="Additional data related to the notification",
        example={
            "order_id": 1234,
            "delivery_time": "30 minutes",
            "tracking_number": "TRK123456"
        }
    )

    model_config = ConfigDict(from_attributes=True)
