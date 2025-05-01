"""
Cart Controller

Handles user requests related to shopping cart operations and delegates
business logic to the cart_service module.

This module performs the following operations:
- Add items to cart
- Retrieve user's cart items
- Update item quantity in cart
- Remove an item from cart
- Clear all items from cart

Access: All endpoints require the user to be authenticated.
"""

# print("CART CONTROLLER MODULE LOADED")

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartItemRead
from app.services import cart_service
from app.db.models.menu_item import MenuItem
import json
import asyncio

# Role: User
async def add_item_to_cart(
    item: CartItemCreate,
    db: AsyncSession,
    current_user
):
    # print("CART CONTROLLER add_item_to_cart CALLED")
    import traceback
    try:
        cart_item = await cart_service.add_item_to_cart(db, item, current_user.id)
        menu_item = await db.get(MenuItem, cart_item.menu_item_id)
        response_data = {
            "id": cart_item.id,
            "user_id": cart_item.user_id,
            "menu_item_id": cart_item.menu_item_id,
            "quantity": cart_item.quantity,
            "special_instructions": cart_item.special_instructions,
            "selected_options": json.loads(cart_item.selected_options) if cart_item.selected_options else None,
            "created_at": cart_item.created_at,
            "updated_at": cart_item.updated_at,
            "menu_item_name": menu_item.name if menu_item else None,
            "menu_item_price": menu_item.price if menu_item else None,
            "option_names": [],  # Populate if you have option logic
            "subtotal": (menu_item.price * cart_item.quantity) if menu_item else 0,
        }
        return CartItemRead(**response_data)
    except Exception as e:
        # print("[CART ADD ERROR]", traceback.format_exc())
        raise


async def get_cart_items(
    db: AsyncSession,
    current_user
):
    # print("CART CONTROLLER get_cart_items CALLED")
    try:
        items = await cart_service.get_cart_items(db, current_user.id)
        from app.db.models.menu_item import MenuItem
        import json
        response = []
        for cart_item in items:
            try:
                menu_item = await db.get(MenuItem, cart_item.menu_item_id)
            except Exception as menu_item_exc:
                # print(f"[ERROR] Failed to fetch menu_item for menu_item_id={cart_item.menu_item_id}: {menu_item_exc}")
                menu_item = None
            # Defensive: ensure all fields are present and valid
            try:
                selected_options = None
                if cart_item.selected_options:
                    try:
                        selected_options = json.loads(cart_item.selected_options)
                    except Exception as so_exc:
                        # print(f"[ERROR] selected_options JSON decode failed: {so_exc}")
                        selected_options = None
                response.append({
                    "id": getattr(cart_item, "id", None),
                    "user_id": getattr(cart_item, "user_id", None),
                    "menu_item_id": getattr(cart_item, "menu_item_id", None),
                    "quantity": getattr(cart_item, "quantity", None),
                    "special_instructions": getattr(cart_item, "special_instructions", None),
                    "selected_options": selected_options,
                    "created_at": getattr(cart_item, "created_at", None),
                    "updated_at": getattr(cart_item, "updated_at", None),
                    "menu_item_name": getattr(menu_item, "name", None) if menu_item else None,
                    "menu_item_price": getattr(menu_item, "price", None) if menu_item else None,
                    "option_names": [],
                    "subtotal": (getattr(menu_item, "price", 0) * getattr(cart_item, "quantity", 0)) if menu_item and getattr(cart_item, "quantity", None) is not None else 0,
                })
            except Exception as dict_exc:
                # print(f"[ERROR] Failed to build cart item dict: {dict_exc}")
                continue
        from app.schemas.cart import CartItemRead
        cart_items = [CartItemRead(**item) for item in response]
        return [item.dict() for item in cart_items]
    except Exception as e:
        import traceback
        # print("[CART GET ERROR]", traceback.format_exc())
        return {"error": str(e), "traceback": traceback.format_exc()}


async def update_cart_item(
    cart_item_id: int,
    quantity: int,
    db: AsyncSession,
    current_user
):
    """
    Update the quantity of a specific cart item.
    Role: User
    """
    cart_item = await cart_service.update_cart_item_quantity(db, cart_item_id, quantity, current_user.id)
    from app.db.models.menu_item import MenuItem
    menu_item = await db.get(MenuItem, cart_item.menu_item_id)
    # Gather selected_options and option_names if present, otherwise None
    selected_options = None
    option_names = None
    if hasattr(cart_item, "selected_options") and cart_item.selected_options:
        import json
        try:
            selected_options = json.loads(cart_item.selected_options) if isinstance(cart_item.selected_options, str) else cart_item.selected_options
        except Exception:
            selected_options = cart_item.selected_options
        # Optionally, resolve option names if you have a model for them
        option_names = []
    response_data = {
        "id": cart_item.id,
        "user_id": cart_item.user_id,
        "menu_item_id": cart_item.menu_item_id,
        "quantity": cart_item.quantity,
        "special_instructions": getattr(cart_item, "special_instructions", None),
        "created_at": cart_item.created_at,
        "updated_at": cart_item.updated_at,
        "menu_item_name": menu_item.name if menu_item else None,
        "menu_item_price": menu_item.price if menu_item else None,
        "selected_options": selected_options,
        "option_names": option_names,
        "subtotal": (menu_item.price * cart_item.quantity) if menu_item else 0,
    }
    return response_data


async def remove_cart_item(
    cart_item_id: int,
    db: AsyncSession,
    current_user
):
    """
    Remove an item from the user's cart.
    Role: User
    """
    result = await cart_service.remove_cart_item(db, cart_item_id, current_user.id)
    return jsonable_encoder(result)


async def clear_user_cart(
    db: AsyncSession,
    current_user
):
    """
    Clear all items from the user's cart.
    Role: User
    """
    result = await cart_service.clear_cart(db, current_user.id)
    # Ensure result is a dict and not a coroutine or other type
    if isinstance(result, dict):
        return result
    elif hasattr(result, '__dict__'):
        return dict(result.__dict__)
    else:
        return {"detail": str(result)}
