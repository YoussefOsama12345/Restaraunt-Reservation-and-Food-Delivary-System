"""
Shopping cart API routes.

Provides endpoints for managing a user's shopping cart, including adding items,
viewing cart contents, updating item quantities, and clearing the cart.
All routes require authenticated user access.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.cart import CartItemCreate, CartItemUpdate, CartItemRead
from app.api.deps import get_current_user, get_db
from app.controllers import cart_controller

router = APIRouter(prefix="/cart", tags=["cart"])


@router.post("/", response_model=CartItemRead)
async def add_item_to_cart(
    item: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Add an item to the authenticated user's shopping cart.
    Role: User
    """
    try:
        return await cart_controller.add_item_to_cart(item, db, current_user)
    except Exception as e:
        import traceback
        print("[CART ROUTE ERROR]", traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/", response_model=List[CartItemRead])
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve all items in the authenticated user's shopping cart.
    Role: User
    """
    try:
        return await cart_controller.get_cart_items(db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{cart_item_id}", response_model=CartItemRead)
async def update_cart_item(
    cart_item_id: int,
    item: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update the quantity of a specific item in the cart.
    Role: User
    """
    try:
        return await cart_controller.update_cart_item(cart_item_id, item.quantity, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{cart_item_id}", response_model=dict)
async def remove_cart_item(
    cart_item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Remove an item from the user's cart.
    Role: User
    """
    try:
        result = await cart_controller.remove_cart_item(cart_item_id, db, current_user)
        # Log and inspect result type for debugging
        import logging
        logging.warning(f"remove_cart_item result type: {type(result)} value: {result}")
        # Defensive: always return a dict
        if isinstance(result, dict):
            return result
        elif hasattr(result, '__dict__'):
            return dict(result.__dict__)
        else:
            return {"detail": str(result)}
    except Exception as e:
        import traceback
        logging.error(f"remove_cart_item error: {traceback.format_exc()}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/", response_model=dict)
async def clear_cart(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Clear all items from the user's cart.
    Role: User
    """
    try:
        result = await cart_controller.clear_user_cart(db, current_user)
        # Log and inspect result type for debugging
        import logging
        logging.warning(f"clear_user_cart result type: {type(result)} value: {result}")
        # Defensive: always return a dict
        if isinstance(result, dict):
            return result
        elif hasattr(result, '__dict__'):
            return dict(result.__dict__)
        else:
            return {"detail": str(result)}
    except Exception as e:
        import traceback
        logging.error(f"clear_cart error: {traceback.format_exc()}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
