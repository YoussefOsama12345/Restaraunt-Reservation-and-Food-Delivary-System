"""
Address Service

Handles business logic for user address book operations:

- Creating new addresses
- Listing saved addresses for a user
- Retrieving a specific address by ID
- Updating an existing address
- Deleting an address
- Retrieving the default address for a user

Role:
- User
"""

from typing import List, Optional
from sqlalchemy.orm import Session

# Placeholder models and schemas
class Address:
    id: int
    user_id: int
    street: str
    city: str
    state: str
    zip_code: str
    is_default: bool

class AddressCreate:
    street: str
    city: str
    state: str
    zip_code: str
    is_default: Optional[bool] = False

class AddressUpdate:
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    is_default: Optional[bool]

def create_address(address_data: AddressCreate, user_id: int) -> Address:
    """
    Create a new delivery or billing address for the user.
    Role: User
    """
    pass

def list_addresses(user_id: int) -> List[Address]:
    """
    List all addresses saved by the user.
    Role: User
    """
    pass

def get_address_by_id(address_id: int, user_id: int) -> Address:
    """
    Retrieve a specific address by its ID for the user.
    Role: User
    """
    pass

def update_address(address_id: int, address_data: AddressUpdate, user_id: int) -> Address:
    """
    Update fields of an existing address.
    Role: User
    """
    pass

def delete_address(address_id: int, user_id: int) -> dict:
    """
    Delete an address by its ID.
    Role: User
    """
    pass

def get_default_address(user_id: int) -> Optional[Address]:
    """
    Retrieve the user's default address, if one is set.
    Role: User
    """
    pass
