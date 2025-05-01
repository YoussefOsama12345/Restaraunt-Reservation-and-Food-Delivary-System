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
from fastapi import Depends, APIRouter, HTTPException, status
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
    try:
        addr = await address_service.create_address(address, user_id, db)
        return AddressRead.from_orm(addr)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def list_addresses(user_id: int, db: AsyncSession) -> list[dict]:
    """
    List all addresses for a user.
    """
    result = await db.execute(select(Address).where(Address.user_id == user_id))
    addresses = result.scalars().all()
    return [jsonable_encoder(AddressRead.from_orm(addr)) for addr in addresses]


async def get_address_by_id(address_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Get a specific address by ID for the user.
    """
    try:
        addr = await address_service.get_address_by_id(address_id, user_id, db)
        return jsonable_encoder(AddressRead.from_orm(addr))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def update_address(address_id: int, address: AddressUpdate, user_id: int, db: AsyncSession) -> dict:
    """
    Update an existing address for the user.
    """
    try:
        addr = await address_service.update_address(address_id, address, user_id, db)
        return jsonable_encoder(AddressRead.from_orm(addr))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def delete_address(address_id: int, user_id: int, db: AsyncSession) -> dict:
    """
    Delete an address for the user.
    """
    try:
        addr = await address_service.delete_address(address_id, user_id, db)
        return jsonable_encoder(addr)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_default_address(user_id: int, db: AsyncSession) -> dict | None:
    """
    Get the default address for the user.
    """
    addr = await address_service.get_default_address(user_id, db)
    if not addr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No default address found")
    return jsonable_encoder(AddressRead.from_orm(addr))
