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

async def create_address(address_data, user_id: int, db: AsyncSession) -> Address:
    """
    Create a new delivery or billing address for the user.
    Role: User
    """
    data = address_data.dict(exclude_unset=True) if hasattr(address_data, 'dict') else dict(address_data)
    data_filtered = {k: v for k, v in data.items() if k in Address.__table__.columns.keys()}
    data_filtered['user_id'] = user_id
    address = Address(**data_filtered)
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


async def update_address(address_id: int, address_data, user_id: int, db: AsyncSession) -> Address:
    """
    Update fields of an existing address.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.id == address_id, Address.user_id == user_id))
    address = result.scalars().first()
    if not address:
        raise Exception("Address not found or unauthorized")
    update_data = address_data.dict(exclude_unset=True) if hasattr(address_data, 'dict') else dict(address_data)
    for field, value in update_data.items():
        if value is not None and hasattr(address, field):
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


async def get_default_address(user_id: int, db: AsyncSession) -> Optional[Address]:
    """
    Retrieve the default address for a user.
    Role: User
    """
    result = await db.execute(select(Address).where(Address.user_id == user_id, Address.is_default == True))
    address = result.scalars().first()
    return address
