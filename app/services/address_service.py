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
# ---
# UPDATED BY AI: Converted all service functions to async using AsyncSession and SQLAlchemy select().
# Ensured all DB operations use await, fixed compatibility with async controller/routes, and improved error handling.
# ---
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.address import Address

# Placeholder models and schemas
class AddressCreate:
    street_address: str
    city: str
    state: str
    postal_code: str
    country: str
    label: str
    is_default: Optional[bool] = False

class AddressUpdate:
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    label: Optional[str]
    is_default: Optional[bool]

async def create_address(address_data: AddressCreate, user_id: int, db: AsyncSession) -> Address:
    """
    Create a new delivery or billing address for the user.
    Role: User
    """
    address = Address(
        user_id=user_id,
        street_address=getattr(address_data, 'street_address', None),
        city=getattr(address_data, 'city', None),
        state=getattr(address_data, 'state', None),
        postal_code=getattr(address_data, 'postal_code', None),
        country=getattr(address_data, 'country', None),
        is_default=getattr(address_data, 'is_default', False),
        label=getattr(address_data, 'label', None)
    )
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address

async def list_addresses(user_id: int, db: AsyncSession) -> list[Address]:
    """
    List all addresses saved by the user.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.user_id == user_id))
    return result.scalars().all()


async def get_address_by_id(address_id: int, user_id: int, db: AsyncSession) -> Address:
    """
    Retrieve a specific address by its ID for the user.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.id == address_id, Address.user_id == user_id))
    address = result.scalars().first()
    if not address:
        raise Exception("Address not found or unauthorized")
    return address


async def update_address(address_id: int, address_data: AddressUpdate, user_id: int, db: AsyncSession) -> Address:
    """
    Update fields of an existing address.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.id == address_id, Address.user_id == user_id))
    address = result.scalars().first()
    if not address:
        raise Exception("Address not found or unauthorized")
    for field, value in address_data.__dict__.items():
        if value is not None:
            setattr(address, field, value)
    await db.commit()
    await db.refresh(address)
    return address


async def delete_address(address_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Delete an address by its ID.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.id == address_id, Address.user_id == user_id))
    address = result.scalars().first()
    if not address:
        raise Exception("Address not found or unauthorized")
    await db.delete(address)
    await db.commit()
    return {"detail": "Address deleted successfully"}


async def get_default_address(user_id: int, db: AsyncSession) -> Address | None:
    """
    Retrieve the default address for a user.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.user_id == user_id, Address.is_default == True))
    address = result.scalars().first()
    return address
