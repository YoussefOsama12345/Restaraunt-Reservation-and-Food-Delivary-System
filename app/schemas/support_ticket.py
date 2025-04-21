from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class SupportTicketBase(BaseModel):
    """
    Base schema for support ticket-related data.

    Attributes:
        user_id (int): The ID of the user submitting the ticket.
        subject (str): The subject of the support ticket.
        message (str): The detailed message describing the issue.
        order_id (Optional[int]): The ID of the related order, if applicable.
        reservation_id (Optional[int]): The ID of the related reservation, if applicable.
        created_at (datetime): The timestamp when the ticket was created.
        status (str): The current status of the ticket (e.g., "open", "in_progress", "resolved").
    """
    user_id: int
    subject: str = Field(..., example="Issue with my order")
    message: str = Field(..., example="I received the wrong item.")
    order_id: Optional[int] = None
    reservation_id: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field("open", example="open")

    model_config = ConfigDict(from_attributes=True)

class SupportTicketCreate(SupportTicketBase):
    """
    Schema for creating a new support ticket.

    Attributes:
        user_id (int): The ID of the user submitting the ticket.
        subject (str): The subject line of the support ticket.
        message (str): Detailed description of the issue.
        order_id (Optional[int]): Associated order ID if ticket is order-related.
        reservation_id (Optional[int]): Associated reservation ID if ticket is reservation-related.
        priority (Optional[str]): Priority level of the ticket.
        category (Optional[str]): Category of the support issue.
        created_at (datetime): Timestamp when the ticket was created.
        status (str): Current status of the ticket.
    """
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user creating the ticket",
        example=1
    )
    subject: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description="Brief subject line describing the issue",
        example="Wrong order received"
    )
    message: str = Field(
        ...,
        min_length=20,
        max_length=1000,
        description="Detailed description of the issue",
        example="I ordered a vegetarian pizza but received a meat lovers pizza instead."
    )
    order_id: Optional[int] = Field(
        None,
        gt=0,
        description="Associated order ID if the ticket is order-related",
        example=123
    )
    reservation_id: Optional[int] = Field(
        None,
        gt=0,
        description="Associated reservation ID if the ticket is reservation-related",
        example=456
    )
    priority: Optional[str] = Field(
        "normal",
        pattern="^(low|normal|high|urgent)$",
        description="Priority level of the ticket",
        example="normal"
    )
    category: Optional[str] = Field(
        None,
        max_length=50,
        description="Category of the support issue",
        example="order_issue"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the ticket was created",
        example="2024-04-18T10:00:00Z"
    )
    status: str = Field(
        "open",
        pattern="^(open|in_progress|resolved|closed)$",
        description="Current status of the ticket",
        example="open"
    )

    model_config = ConfigDict(from_attributes=True)

class SupportTicketUpdate(SupportTicketBase):
    """
    Schema for updating an existing support ticket.
    All fields are optional to allow partial updates.

    Attributes:
        subject (Optional[str]): Updated subject of the ticket
        message (Optional[str]): Updated message content
        status (Optional[str]): Updated ticket status
        priority (Optional[str]): Updated priority level
        category (Optional[str]): Updated ticket category
        updated_by (str): Who is making the update
        update_reason (Optional[str]): Reason for the update
    """
    subject: Optional[str] = Field(
        None,
        min_length=5,
        max_length=100,
        description="Updated subject line of the ticket",
        example="Updated: Wrong order received"
    )
    message: Optional[str] = Field(
        None,
        min_length=20,
        max_length=1000,
        description="Updated description of the issue",
        example="Additional details about the wrong order received"
    )
    status: Optional[str] = Field(
        None,
        pattern="^(open|in_progress|resolved|closed)$",
        description="Updated status of the ticket",
        example="in_progress"
    )
    priority: Optional[str] = Field(
        None,
        pattern="^(low|normal|high|urgent)$",
        description="Updated priority level",
        example="high"
    )
    category: Optional[str] = Field(
        None,
        max_length=50,
        description="Updated category of the issue",
        example="order_issue"
    )
    updated_by: str = Field(
        ...,
        pattern="^(admin|support|customer)$",
        description="Who is making the update",
        example="support"
    )
    update_reason: Optional[str] = Field(
        None,
        max_length=200,
        description="Reason for updating the ticket",
        example="Escalating priority due to customer follow-up"
    )

    model_config = ConfigDict(from_attributes=True)

class SupportTicketRead(SupportTicketBase):
    """
    Schema for returning support ticket data to the client.

    Attributes:
        id (int): Unique identifier for the support ticket
        user_id (int): ID of the user who created the ticket
        subject (str): Subject line of the ticket
        message (str): Detailed description of the issue
        order_id (Optional[int]): Associated order ID
        reservation_id (Optional[int]): Associated reservation ID
        priority (Optional[str]): Ticket priority level
        category (Optional[str]): Support issue category
        status (str): Current ticket status
        created_at (datetime): Creation timestamp
        updated_at (Optional[datetime]): Last update timestamp
        resolution_time (Optional[int]): Resolution time in minutes
        assigned_to (Optional[str]): Assigned staff member
        response_count (Optional[int]): Number of staff responses
        last_response_at (Optional[datetime]): Last response timestamp
        customer_satisfaction (Optional[int]): Customer satisfaction rating (1-5)
        feedback (Optional[str]): Customer feedback on ticket resolution
    """
    id: int = Field(
        ...,
        description="Unique identifier for the support ticket",
        example=1
    )
    user_id: int = Field(
        ...,
        gt=0,
        description="ID of the user who created the ticket",
        example=123
    )
    subject: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description="Subject line of the ticket",
        example="Issue with delivery order #456"
    )
    message: str = Field(
        ...,
        min_length=20,
        max_length=1000,
        description="Detailed description of the issue",
        example="My order arrived cold and items were missing"
    )
    order_id: Optional[int] = Field(
        None,
        gt=0,
        description="Associated order ID",
        example=456
    )
    reservation_id: Optional[int] = Field(
        None,
        gt=0,
        description="Associated reservation ID",
        example=789
    )
    priority: Optional[str] = Field(
        None,
        pattern="^(low|normal|high|urgent)$",
        description="Priority level of the ticket",
        example="high"
    )
    category: Optional[str] = Field(
        None,
        max_length=50,
        description="Category of the support issue",
        example="delivery_issue"
    )
    status: str = Field(
        ...,
        pattern="^(open|in_progress|resolved|closed)$",
        description="Current status of the ticket",
        example="in_progress"
    )
    created_at: datetime = Field(
        ...,
        description="When the ticket was created",
        example="2024-04-18T10:00:00Z"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="When the ticket was last updated",
        example="2024-04-18T15:30:00Z"
    )
    resolution_time: Optional[int] = Field(
        None,
        ge=0,
        description="Time taken to resolve the ticket in minutes",
        example=45
    )
    assigned_to: Optional[str] = Field(
        None,
        pattern="^[a-zA-Z0-9_-]+$",
        description="Staff member assigned to the ticket",
        example="support_agent_1"
    )
    response_count: Optional[int] = Field(
        0,
        ge=0,
        description="Number of staff responses to the ticket",
        example=3
    )
    last_response_at: Optional[datetime] = Field(
        None,
        description="Timestamp of the last response",
        example="2024-04-18T14:30:00Z"
    )
    customer_satisfaction: Optional[int] = Field(
        None,
        ge=1,
        le=5,
        description="Customer satisfaction rating (1-5)",
        example=4
    )
    feedback: Optional[str] = Field(
        None,
        max_length=500,
        description="Customer feedback on ticket resolution",
        example="Issue was resolved quickly and professionally"
    )

    model_config = ConfigDict(from_attributes=True)
