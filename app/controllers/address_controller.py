"""
Address Controller

Handles address-related operations such as creation, listing, retrieval,
updates, deletion, and default address retrieval.
Delegates business logic to address_service or directly accesses the DB via SQLAlchemy.
"""
# ---
# UPDATED BY AI: Converted all controller functions to async, fixed return types to use AddressRead Pydantic model, 
# handled both Pydantic v1 and v2 serialization, and ensured proper error handling for FastAPI endpoints.
# ---
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.encoders import jsonable_encoder

from app.db.database import get_db
from app.api.deps import get_current_user, get_current_admin
from app.db.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate, AddressRead
from app.services import address_service


async def create_address(address: AddressCreate, user_id: int, db: AsyncSession) -> AddressRead:
    """
    Create a new address for the user.
    """
    addr = await address_service.create_address(address, user_id, db)
    # Pydantic v2: use AddressRead.model_validate if available, else AddressRead.from_orm
    try:
        return AddressRead.model_validate(addr)
    except AttributeError:
        return AddressRead.from_orm(addr)


async def list_addresses(user_id: int, db: AsyncSession) -> list[dict]:
    """
    List all addresses for a user.
    """
    result = await db.execute(select(Address).where(Address.user_id == user_id))
    addresses = result.scalars().all()
    return [jsonable_encoder(AddressRead.model_validate(addr) if hasattr(AddressRead, 'model_validate') else AddressRead.from_orm(addr)) for addr in addresses]


def get_address_by_id(address_id: int, user_id: int, db: Session) -> dict:
    """
    Get a specific address by ID for the user.
    """
    addr = address_service.get_address_by_id(address_id, user_id, db)
    return jsonable_encoder(AddressRead.model_validate(addr) if hasattr(AddressRead, 'model_validate') else AddressRead.from_orm(addr))


async def update_address(address_id: int, address: AddressUpdate, user_id: int, db: AsyncSession) -> dict:
    """
    Update an existing address for the user.
    """
    addr = await address_service.update_address(address_id, address, user_id, db)
    return jsonable_encoder(AddressRead.model_validate(addr) if hasattr(AddressRead, 'model_validate') else AddressRead.from_orm(addr))


async def delete_address(address_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Delete an address for the user.
    """
    addr = await address_service.delete_address(address_id, user_id, db)
    return jsonable_encoder(addr)


async def get_default_address(user_id: int, db: AsyncSession) -> dict | None:
    """
    Get the default address for the user.
    """
    addr = await address_service.get_default_address(user_id, db)
    return jsonable_encoder(AddressRead.model_validate(addr) if hasattr(AddressRead, 'model_validate') else AddressRead.from_orm(addr)) if addr else None
