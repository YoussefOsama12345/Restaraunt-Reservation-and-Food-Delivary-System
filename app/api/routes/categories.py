"""
Address Controller

Manages address book operations for authenticated users, including:
- Creating new addresses
- Listing saved addresses
- Updating existing addresses
- Deleting addresses
- Retrieving the default address

Delegates business logic to address_service.

Access: All endpoints require authenticated users.
"""

from fastapi import APIRouter
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


def create_address():
    """
    Create a new delivery or billing address.
    Role: User
    """
    pass


def get_user_addresses():
    """
    Retrieve all addresses saved by the user.
    Role: User
    """
    pass


def update_address():
    """
    Update an existing address by its ID.
    Role: User
    """
    pass


def delete_address():
    """
    Delete an address from the user's account.
    Role: User
    """
    pass


def get_default_address():
    """
    Retrieve the default address for the user.
    Role: User
    """
    pass
