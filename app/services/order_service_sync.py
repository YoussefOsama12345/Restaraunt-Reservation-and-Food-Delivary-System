"""
Synchronous Order Service

This module provides synchronous versions of the order service functions
to handle cases where async operations cannot be used due to MissingGreenlet errors.
"""

from typing import List, Optional, Dict
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.session import SessionLocal
from datetime import datetime

def get_order_sync(order_id: int, user_id: int) -> dict:
    """
    Synchronous version of get_order.
    Retrieves a specific order by its ID.

    Args:
        order_id (int): ID of the order to retrieve.
        user_id (int): ID of the user requesting the order.

    Returns:
        dict: The requested order object.

    Role: User
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Use synchronous SQLAlchemy query
        order = db.query(Order).options(
            joinedload(Order.order_items)
        ).filter(
            and_(Order.id == order_id, Order.user_id == user_id)
        ).first()
        
        if not order:
            raise Exception("Order not found or unauthorized")
            
        # Convert to dictionary
        order_dict = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
        if hasattr(order, 'payment_method') and order.payment_method is not None:
            order_dict['payment_method'] = order.payment_method
        else:
            order_dict['payment_method'] = 'unknown'
            
        # Handle order items
        order_dict['items'] = []
        if order.order_items:
            for oi in order.order_items:
                item_dict = {c.name: getattr(oi, c.name) for c in OrderItem.__table__.columns}
                order_dict['items'].append(item_dict)
                
        return order_dict
    finally:
        db.close()

def list_orders_sync(user_id: Optional[int] = None) -> List[dict]:
    """
    Synchronous version of list_orders.
    Lists orders, optionally filtered by user ID.

    Args:
        user_id (Optional[int]): If provided, returns orders for this user only.

    Returns:
        List[dict]: List of orders.

    Role: User
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Build query
        query = db.query(Order).options(joinedload(Order.order_items))
        
        # Filter by user if specified
        if user_id:
            query = query.filter(Order.user_id == user_id)
            
        # Execute query
        orders = query.all()
        
        # Convert to dictionaries
        order_dicts = []
        for order in orders:
            order_dict = {c.name: getattr(order, c.name) for c in Order.__table__.columns}
            if hasattr(order, 'payment_method') and order.payment_method is not None:
                order_dict['payment_method'] = order.payment_method
            else:
                order_dict['payment_method'] = 'unknown'
                
            # Handle order items
            order_dict['items'] = []
            if order.order_items:
                for oi in order.order_items:
                    item_dict = {c.name: getattr(oi, c.name) for c in OrderItem.__table__.columns}
                    order_dict['items'].append(item_dict)
                    
            order_dicts.append(order_dict)
            
        return order_dicts
    finally:
        db.close()
