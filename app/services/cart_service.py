"""
Cart Service

Handles shopping cart functionality for authenticated users.

Includes:
- Adding items to cart
- Retrieving current cart items
- Updating quantities of cart items
- Removing individual items or clearing the cart

Role:
- User
"""

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.cart import CartItem as CartItemModel
from app.db.models.menu_item import MenuItem
from sqlalchemy import text
import json
from app.schemas.cart import CartItemCreate
from fastapi import HTTPException


async def add_item_to_cart(db: AsyncSession, item_data: CartItemCreate, user_id: int) -> CartItemModel:
    """
    Add an item to the user's cart. If the item already exists, update the quantity.
    """
    # Check if menu item exists
    menu_item_result = await db.execute(select(MenuItem).where(MenuItem.id == item_data.menu_item_id))
    if not menu_item_result.scalars().first():
        raise HTTPException(status_code=404, detail="Menu item does not exist.")

    # Check if the item is already in the cart
    result = await db.execute(
        select(CartItemModel).where(
            CartItemModel.user_id == user_id,
            CartItemModel.menu_item_id == item_data.menu_item_id,
            CartItemModel.special_instructions == getattr(item_data, 'special_instructions', None),
            CartItemModel.selected_options == json.dumps(getattr(item_data, 'selected_options', None)) if getattr(item_data, 'selected_options', None) is not None else None
        )
    )
    cart_item = result.scalars().first()
    if cart_item:
        cart_item.quantity += item_data.quantity
        await db.commit()
        await db.refresh(cart_item)
        return cart_item
    # Otherwise, create a new cart item
    new_cart_item = CartItemModel(
        user_id=user_id,
        menu_item_id=item_data.menu_item_id,
        quantity=item_data.quantity,
        special_instructions=getattr(item_data, 'special_instructions', None),
        selected_options=json.dumps(getattr(item_data, 'selected_options', None)) if getattr(item_data, 'selected_options', None) is not None else None
    )
    db.add(new_cart_item)
    await db.commit()
    await db.refresh(new_cart_item)
    return new_cart_item


async def get_cart_items(db: AsyncSession, user_id: int) -> list[CartItemModel]:
    """
    Get all items in the user's shopping cart.
    """
    result = await db.execute(select(CartItemModel).where(CartItemModel.user_id == user_id))
    return result.scalars().all()


async def update_cart_item_quantity(db: AsyncSession, cart_item_id: int, quantity: int, user_id: int) -> CartItemModel:
    """
    Update the quantity of a specific cart item.
    """
    result = await db.execute(select(CartItemModel).where(CartItemModel.id == cart_item_id, CartItemModel.user_id == user_id))
    cart_item = result.scalars().first()
    if not cart_item:
        raise Exception("Cart item not found or unauthorized")
    cart_item.quantity = quantity
    await db.commit()
    await db.refresh(cart_item)
    return cart_item


async def remove_cart_item(db: AsyncSession, cart_item_id: int, user_id: int) -> dict:
    """
    Remove a specific item from the user's cart.
    """
    result = await db.execute(select(CartItemModel).where(CartItemModel.id == cart_item_id, CartItemModel.user_id == user_id))
    cart_item = result.scalars().first()
    if not cart_item:
        raise Exception("Cart item not found or unauthorized")
    await db.delete(cart_item)
    await db.commit()
    return {"detail": "Cart item removed successfully"}


async def clear_cart(db: AsyncSession, user_id: int) -> dict:
    """
    Clear all items from the user's cart.
    """
    result = await db.execute(select(CartItemModel).where(CartItemModel.user_id == user_id))
    items = result.scalars().all()
    for item in items:
        await db.delete(item)
    await db.commit()
    return {"detail": "Cart cleared successfully"}
