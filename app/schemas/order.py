from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class OrderItem(BaseModel):
    """
    Represents an item in an order.

    Attributes:
        menu_item_id (int): The ID of the menu item being ordered.
        quantity (int): The quantity of the menu item being ordered.
    """
    menu_item_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    """
    Base schema for order-related data.

    Attributes:
        status (Optional[str]): The current status of the order (default is "pending").
        total_amount (float): The total amount for the order.
        payment_method (str): The method of payment used for the order.
        delivery_address_id (Optional[int]): The ID of the delivery address associated with the order.
    """
    status: Optional[str] = Field("pending", example="confirmed")
    total_amount: float = Field(..., example=42.99)
    payment_method: str = Field(..., example="credit_card")
    delivery_address_id: Optional[int] = Field(None)

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(OrderBase):
    """
    Schema for creating a new order.

    Inherits from OrderBase and adds the items being ordered.

    Attributes:
        items (List[OrderItem]): A list of items included in the order. Must contain at least one item.
        total_amount (float): The total amount for the order. Must be greater than 0.
        payment_method (str): The method of payment used for the order. Must be one of: credit_card, cash, online_payment.
        delivery_address_id (Optional[int]): The ID of the delivery address associated with the order.
        status (Optional[str]): The initial status of the order. Defaults to "pending".
    """
    items: List[OrderItem] = Field(
        ...,
        description="List of items in the order",
        min_items=1,
        example=[{"menu_item_id": 1, "quantity": 2}]
    )
    total_amount: float = Field(
        ...,
        gt=0,
        description="Total amount of the order",
        example=42.99
    )
    payment_method: str = Field(
        ...,
        description="Payment method for the order",
        pattern="^(credit_card|cash|online_payment)$",
        example="credit_card"
    )
    delivery_address_id: Optional[int] = Field(
        None,
        description="ID of the delivery address",
        ge=1,
        example=1
    )
    status: Optional[str] = Field(
        "pending",
        description="Initial status of the order",
        pattern="^(pending|confirmed|preparing|out_for_delivery|delivered|cancelled)$",
        example="pending"
    )

    model_config = ConfigDict(from_attributes=True)


class OrderUpdateStatus(BaseModel):
    """
    Schema for updating the status of an existing order.

    Attributes:
        status (str): The new status of the order. Must be one of:
            - pending: Initial state when order is created
            - confirmed: Order has been confirmed by restaurant
            - preparing: Order is being prepared
            - out_for_delivery: Order is being delivered
            - delivered: Order has been delivered
            - cancelled: Order has been cancelled
        cancellation_reason (Optional[str]): Required if status is 'cancelled'
        updated_by (str): Who is updating the status (e.g., 'restaurant', 'customer', 'delivery_person')
        notes (Optional[str]): Additional notes about the status update
    """
    status: str = Field(
        ...,
        pattern="^(pending|confirmed|preparing|out_for_delivery|delivered|cancelled)$",
        description="New status of the order"
    )
    cancellation_reason: Optional[str] = Field(
        None,
        description="Reason for cancellation if status is 'cancelled'",
        min_length=5,
        max_length=500
    )
    updated_by: str = Field(
        ...,
        pattern="^(restaurant|customer|delivery_person|system)$",
        description="Who is updating the status"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes about the status update",
        max_length=500
    )

    model_config = ConfigDict(from_attributes=True)

    def validate_cancellation(self) -> bool:
        """
        Validates that cancellation_reason is provided when status is 'cancelled'.
        
        Returns:
            bool: True if validation passes, False otherwise
        """
        if self.status == "cancelled" and not self.cancellation_reason:
            return False
        return True


class OrderRead(OrderBase):
    """
    Schema for returning order data to the client/customer.
    Inherits from OrderBase and includes additional fields for order identification.

    Attributes:
        id (int): The unique identifier for the order.
        user_id (int): The ID of the user who placed the order.
        created_at (datetime): The timestamp when the order was created.
        updated_at (datetime): The timestamp when the order was last updated.
        order_number (str): A unique order number for customer reference.
        items (List[OrderItem]): A list of items included in the order.
        estimated_delivery_time (Optional[datetime]): Estimated time of delivery.
        actual_delivery_time (Optional[datetime]): Actual time of delivery.
        delivery_person_id (Optional[int]): ID of the delivery person assigned.
        restaurant_id (int): ID of the restaurant the order is from.
    """
    id: int = Field(
        ...,
        description="Unique identifier for the order"
        )
    user_id: int = Field(
        ..., 
        description="ID of the user who placed the order"
        )
    created_at: datetime = Field(
        ..., 
        description="When the order was created"
        )
    updated_at: datetime = Field(
        ..., 
        description="When the order was last updated"
        )
    order_number: str = Field(
        ..., 
        description="Unique order number for reference"
        )
    items: List[OrderItem] = Field(..., 
        description="List of items in the order"
        )
    estimated_delivery_time: Optional[datetime] = Field(
        None,
        description="Estimated time of delivery"
    )
    actual_delivery_time: Optional[datetime] = Field(
        None,
        description="Actual time of delivery"
    )
    delivery_person_id: Optional[int] = Field(
        None,
        description="ID of the delivery person assigned"
    )
    restaurant_id: int = Field(
        ..., 
        description="ID of the restaurant"
        )

    model_config = ConfigDict(from_attributes=True)
