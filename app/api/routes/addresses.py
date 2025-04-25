"""
User address book API routes.

Provides endpoints for authenticated users to manage delivery and billing addresses.
Supports creation, retrieval, updating, and deletion of address records,
enabling multi-address accounts for flexible deliveries.
"""
# ---
# UPDATED BY AI: Made all route handlers async, used AsyncSession, fixed imports, and ensured all endpoints await controller functions.
# ---
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.address import AddressCreate, AddressUpdate, AddressRead
from app.api.deps import get_current_user, get_db
from app.controllers import address_controller

router = APIRouter(tags=["Addresses"])


@router.post("/", response_model=AddressRead)
async def create_address(
    address: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Create a new delivery or billing address for the authenticated user.
    Role: User
    """
    try:
        return await address_controller.create_address(address, current_user.id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[AddressRead])
async def get_user_addresses(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve all saved addresses for the authenticated user.
    Role: User
    """
    return await address_controller.list_addresses(current_user.id, db)


@router.put("/{address_id}", response_model=AddressRead)
async def update_address(
    address_id: int,
    address: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update an existing address by its ID for the authenticated user.
    Role: User
    """
    try:
        return await address_controller.update_address(address_id, address, current_user.id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{address_id}", response_model=dict)
async def delete_address(
    address_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete a saved address by its ID for the authenticated user.
    Role: User
    """
    try:
        return await address_controller.delete_address(address_id, current_user.id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/default", response_model=AddressRead)
async def get_default_address(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve the default address for the authenticated user.
    Role: User
    """
    address = await address_controller.get_default_address(current_user.id, db)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No default address found"
        )
    return address
