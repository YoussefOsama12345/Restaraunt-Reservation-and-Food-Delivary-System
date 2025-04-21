"""
Order item API routes.

Handles adding, retrieving, updating, and deleting individual items 
within a food order. All endpoints require user authentication.
"""

from fastapi import APIRouter
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/order-items", tags=["order-items"])


def add_order_item(order_id: int, item_data, current_user):
    """
    Add a new item to an existing order.
    Role: User
    """
    pass


def get_order_item(item_id: int, current_user):
    """
    Retrieve a specific item from an order.
    Role: User
    """
    pass


def list_order_items(order_id: int, current_user):
    """
    List all items for a specific order.
    Role: User
    """
    pass


def update_order_item(item_id: int, update_data, current_user):
    """
    Update the quantity or special instructions of an item in an order.
    Role: User
    """
    pass


def delete_order_item(item_id: int, current_user):
    """
    Remove an item from an order.
    Role: User
    """
    pass
