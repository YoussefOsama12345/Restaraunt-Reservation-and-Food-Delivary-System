"""
Synchronous Order Item Service

This module provides synchronous versions of the order item service functions
to handle cases where async operations cannot be used due to MissingGreenlet errors.
"""

from typing import List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.db.models.order_item import OrderItem
from app.db.models.order import Order
from app.db.session import SessionLocal
from fastapi import HTTPException, status

def list_order_items_sync(order_id: int, user_id: int) -> List[dict]:
    """
    Synchronous version of list_order_items.
    Lists all items in a specific order.
    
    Args:
        order_id (int): ID of the order to list items for
        user_id (int): ID of the user requesting the items
        
    Returns:
        List[dict]: List of order items
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Use synchronous SQLAlchemy query
        items = db.query(OrderItem).join(Order).filter(
            OrderItem.order_id == order_id,
            Order.user_id == user_id
        ).all()
        
        # Convert to dictionary format
        return [{c.name: getattr(item, c.name) for c in OrderItem.__table__.columns} 
                for item in items]
    except Exception as e:
        print(f"Error in list_order_items_sync: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close()

def get_order_item_sync(item_id: int, user_id: int) -> dict:
    """
    Synchronous version of get_order_item.
    Retrieves a specific order item by ID.
    
    Args:
        item_id (int): ID of the order item to retrieve
        user_id (int): ID of the user requesting the item
        
    Returns:
        dict: The requested order item
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Use synchronous SQLAlchemy query
        order_item = db.query(OrderItem).join(Order).filter(
            OrderItem.id == item_id,
            Order.user_id == user_id
        ).first()
        
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                               detail="Order item not found or unauthorized")
        
        # Convert to dictionary
        return {c.name: getattr(order_item, c.name) for c in OrderItem.__table__.columns}
    finally:
        db.close()

def add_order_item_sync(order_id: int, item_data: dict, user_id: int) -> dict:
    """
    Synchronous version of add_order_item.
    Adds a new item to an existing order.
    
    Args:
        order_id (int): ID of the order to add item to
        item_data (dict): Data for the new order item
        user_id (int): ID of the user adding the item
        
    Returns:
        dict: The created order item
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Check if order exists and belongs to user
        order = db.query(Order).filter(
            Order.id == order_id,
            Order.user_id == user_id
        ).first()
        
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                               detail="Order not found or unauthorized")
        
        # Create new order item
        order_item = OrderItem(order_id=order_id, **item_data)
        db.add(order_item)
        db.commit()
        db.refresh(order_item)
        
        # Convert to dictionary
        return {c.name: getattr(order_item, c.name) for c in OrderItem.__table__.columns}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close()

def update_order_item_sync(item_id: int, update_data: dict, user_id: int) -> dict:
    """
    Synchronous version of update_order_item.
    Updates an existing order item.
    
    Args:
        item_id (int): ID of the order item to update
        update_data (dict): New data for the order item
        user_id (int): ID of the user updating the item
        
    Returns:
        dict: The updated order item
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Check if order item exists and belongs to user
        order_item = db.query(OrderItem).join(Order).filter(
            OrderItem.id == item_id,
            Order.user_id == user_id
        ).first()
        
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                               detail="Order item not found or unauthorized")
        
        # Update fields
        for field, value in update_data.items():
            if value is not None and hasattr(order_item, field):
                setattr(order_item, field, value)
        
        db.commit()
        db.refresh(order_item)
        
        # Convert to dictionary
        return {c.name: getattr(order_item, c.name) for c in OrderItem.__table__.columns}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close()

def delete_order_item_sync(item_id: int, user_id: int) -> dict:
    """
    Synchronous version of delete_order_item.
    Deletes an order item.
    
    Args:
        item_id (int): ID of the order item to delete
        user_id (int): ID of the user deleting the item
        
    Returns:
        dict: Confirmation message
    """
    # Create a synchronous session
    db = SessionLocal()
    try:
        # Check if order item exists and belongs to user
        order_item = db.query(OrderItem).join(Order).filter(
            OrderItem.id == item_id,
            Order.user_id == user_id
        ).first()
        
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                               detail="Order item not found or unauthorized")
        
        # Delete the item
        db.delete(order_item)
        db.commit()
        
        # Return confirmation
        return {"message": "Order item deleted successfully", "id": item_id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close()
