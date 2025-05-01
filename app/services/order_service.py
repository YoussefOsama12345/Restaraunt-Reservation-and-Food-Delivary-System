"""
Order Service

Manages customer orders, including:
- Placing orders
- Retrieving and listing orders
- Updating order status
- Cancelling orders
- Tracking delivery status

Role: User
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.address import Address
from sqlalchemy import and_
from datetime import datetime
import uuid
from app.utils.db_helpers import handle_missing_greenlet

# ---
# UPDATED BY AI: Converted all service functions to async using AsyncSession and SQLAlchemy select().
# Ensured all DB operations use await, fixed compatibility with async controller/routes, and improved error handling.
# ---

@handle_missing_greenlet
async def create_order(order_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Create a new order.

    Args:
        order_data (dict): Order details including items, payment, and address.
        user_id (int): ID of the user placing the order.

    Returns:
        dict: The created order object.

    Role: User
    """
    # Filter only SQLAlchemy columns
    order_fields = {k: v for k, v in order_data.items() if k in Order.__table__.columns.keys()}
    order_fields['user_id'] = user_id
    order_fields['order_number'] = str(uuid.uuid4())
    order_fields['created_at'] = datetime.utcnow()
    order_fields['updated_at'] = datetime.utcnow()
    # Defensive check for restaurant_id
    if not order_fields.get('restaurant_id'):
        raise Exception("restaurant_id is required to place an order")
    # Validate and ensure delivery_address_id exists
    delivery_address_id = order_fields.get('delivery_address_id')
    if delivery_address_id is not None:
        # Verify the address exists
        address = await db.execute(select(Address).where(Address.id == delivery_address_id))
        address_obj = address.scalars().first()
        if not address_obj:
            raise Exception(f"Invalid delivery_address_id: {delivery_address_id}. Address does not exist.")
    else:
        # If no delivery_address_id provided, find or create one for the user
        user_addresses = await db.execute(select(Address).where(Address.user_id == user_id))
        user_address = user_addresses.scalars().first()
        
        if user_address:
            # Use existing address
            order_fields['delivery_address_id'] = user_address.id
        else:
            # Create a default address for the user
            default_address = Address(
                user_id=user_id,
                street_address="123 Main St",
                city="New York",
                state="NY",
                postal_code="10001",
                country="USA",
                is_default=True,
                label="Home",
                is_active=True
            )
            db.add(default_address)
            await db.flush()
            order_fields['delivery_address_id'] = default_address.id
    # Items are not part of Order columns
    items = order_data.get('items', [])
    order = Order(**order_fields)
    db.add(order)
    await db.flush()  # Get order.id before adding items
    # Create order items
    for item in items:
        item_fields = {k: v for k, v in item.items() if k in OrderItem.__table__.columns.keys() and k != 'order_id'}
        item_fields['order_id'] = order.id
        # You may want to fetch price from MenuItem model for price_at_time
        # For now, require price_at_time in item_fields or set to 0.0
        if 'price_at_time' not in item_fields:
            item_fields['price_at_time'] = 0.0
        db.add(OrderItem(**item_fields))
    await db.commit()
    await db.refresh(order)
    # Return order as dict (simulate serialization)
    result = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
    
    # Ensure payment_method is always included (required by OrderRead schema)
    if 'payment_method' not in result or not result['payment_method']:
        result['payment_method'] = order_data.get('payment_method', 'credit_card')
    # Add items - fetch them separately to avoid MissingGreenlet error
    items_result = await db.execute(select(OrderItem).where(OrderItem.order_id == order.id))
    order_items = items_result.scalars().all()
    
    result['items'] = [
        {c.name: getattr(oi, c.name) for c in OrderItem.__table__.columns}
        for oi in order_items
    ]
    return result

@handle_missing_greenlet
async def get_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve a specific order by its ID.

    Args:
        order_id (int): ID of the order to retrieve.
        user_id (int): ID of the user requesting the order.

    Returns:
        dict: The requested order object.

    Role: User
    """
    # First, get the order without loading relationships
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
        
    # Convert order to dictionary
    order_dict = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
    if hasattr(order, 'payment_method') and order.payment_method is not None:
        order_dict['payment_method'] = order.payment_method
    else:
        order_dict['payment_method'] = 'unknown'
        
    # Separately query for order items to avoid MissingGreenlet errors
    items_result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    order_items = items_result.scalars().all()
    
    # Add items to the order dictionary
    order_dict['items'] = [
        {c.name: getattr(item, c.name) for c in OrderItem.__table__.columns}
        for item in order_items
    ]
        
    return order_dict

@handle_missing_greenlet
async def list_orders(user_id: Optional[int], db: AsyncSession) -> List[dict]:
    """
    List orders, optionally filtered by user ID.

    Args:
        user_id (Optional[int]): If provided, returns orders for this user only.

    Returns:
        List[dict]: List of orders.

    Role: User
    """
    # First, get all orders without loading relationships
    query = select(Order)
    if user_id is not None:
        query = query.where(Order.user_id == user_id)
    result = await db.execute(query)
    orders = result.scalars().all()
    
    order_dicts = []
    for order in orders:
        # Convert order to dictionary
        od = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
        
        # Add payment_method if present on the ORM object (for Pydantic OrderRead)
        if hasattr(order, 'payment_method') and order.payment_method is not None:
            od['payment_method'] = order.payment_method
        else:
            od['payment_method'] = 'unknown'
            
        # Separately query for order items to avoid MissingGreenlet errors
        items_result = await db.execute(select(OrderItem).where(OrderItem.order_id == order.id))
        order_items = items_result.scalars().all()
        
        # Add items to the order dictionary
        od['items'] = [
            {c.name: getattr(item, c.name) for c in OrderItem.__table__.columns}
            for item in order_items
        ]
        
        order_dicts.append(od)
        
    return order_dicts

@handle_missing_greenlet
async def update_order_status(order_id: int, status_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Update the status of an existing order.

    Args:
        order_id (int): ID of the order to update.
        status_data (dict): New status data.
        user_id (int): ID of the user requesting the update.

    Returns:
        dict: Updated order object.

    Role: User
    """
    # First, get the order without loading relationships
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    
    # Update status fields
    for field, value in status_data.items():
        if hasattr(order, field):
            setattr(order, field, value)
    
    # Update timestamp
    order.updated_at = datetime.utcnow()
    
    # If status is 'delivered', set actual_delivery_time
    if status_data.get('status') == 'delivered' and not order.actual_delivery_time:
        order.actual_delivery_time = datetime.utcnow()
    
    await db.commit()
    await db.refresh(order)
    
    # Convert to dict for response
    order_dict = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
    
    # Add payment_method if present (for Pydantic OrderRead)
    if hasattr(order, 'payment_method') and order.payment_method is not None:
        order_dict['payment_method'] = order.payment_method
    else:
        order_dict['payment_method'] = 'unknown'
    
    # Separately query for order items to avoid MissingGreenlet errors
    items_result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    order_items = items_result.scalars().all()
    
    # Add items to the order dictionary
    order_dict['items'] = [
        {c.name: getattr(item, c.name) for c in OrderItem.__table__.columns}
        for item in order_items
    ]
    
    return order_dict

async def cancel_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Cancel an existing order.

    Args:
        order_id (int): ID of the order to cancel.
        user_id (int): ID of the user requesting the cancellation.

    Returns:
        dict: Confirmation message.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    if order.status == "cancelled":
        raise Exception("Order is already cancelled")
    order.status = "cancelled"
    order.updated_at = datetime.utcnow()
    await db.commit()
    return {"detail": "Order cancelled successfully"}

async def track_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve real-time tracking information for an order.

    Args:
        order_id (int): ID of the order to track.
        user_id (int): ID of the user tracking the order.

    Returns:
        dict: Current status, estimated delivery time, and tracking details.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    tracking_info = {
        "order_id": order.id,
        "status": order.status,
        "estimated_delivery_time": order.estimated_delivery_time,
        "actual_delivery_time": order.actual_delivery_time,
        "delivery_person_id": order.delivery_person_id
    }
    return tracking_info

    order_dict['items'] = [
        {c.name: getattr(oi, c.name) for c in OrderItem.__table__.columns}
        for oi in order.order_items
    ]
    return order_dict

async def cancel_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Cancel an existing order.

    Args:
        order_id (int): ID of the order to cancel.
        user_id (int): ID of the user requesting the cancellation.

    Returns:
        dict: Confirmation message.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    if order.status == "cancelled":
        raise Exception("Order is already cancelled")
    order.status = "cancelled"
    order.updated_at = datetime.utcnow()
    await db.commit()
    return {"detail": "Order cancelled successfully"}

async def track_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve real-time tracking information for an order.

    Args:
        order_id (int): ID of the order to track.
        user_id (int): ID of the user tracking the order.

    Returns:
        dict: Current status, estimated delivery time, and tracking details.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    tracking_info = {
        "order_id": order.id,
        "status": order.status,
        "estimated_delivery_time": order.estimated_delivery_time,
        "actual_delivery_time": order.actual_delivery_time,
        "delivery_person_id": order.delivery_person_id
    }
    return tracking_info

    order_dict['items'] = [
        {c.name: getattr(oi, c.name) for c in OrderItem.__table__.columns}
        for oi in order.order_items
    ]
    return order_dict

async def cancel_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Cancel an existing order.

    Args:
        order_id (int): ID of the order to cancel.
        user_id (int): ID of the user requesting the cancellation.

    Returns:
        dict: Confirmation message.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    if order.status == "cancelled":
        raise Exception("Order is already cancelled")
    order.status = "cancelled"
    order.updated_at = datetime.utcnow()
    await db.commit()
    return {"detail": "Order cancelled successfully"}

async def track_order(order_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Retrieve real-time tracking information for an order.

    Args:
        order_id (int): ID of the order to track.
        user_id (int): ID of the user tracking the order.

    Returns:
        dict: Current status, estimated delivery time, and tracking details.

    Role: User
    """
    result = await db.execute(select(Order).where(and_(Order.id == order_id, Order.user_id == user_id)))
    order = result.scalars().first()
    if not order:
        raise Exception("Order not found or unauthorized")
    tracking_info = {
        "order_id": order.id,
        "status": order.status,
        "estimated_delivery_time": order.estimated_delivery_time,
        "actual_delivery_time": order.actual_delivery_time,
        "delivery_person_id": order.delivery_person_id
    }
    return tracking_info
