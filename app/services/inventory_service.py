"""
Inventory Service

Provides logic for managing restaurant inventory items such as ingredients,
supplies, or packaging.

Includes:
- Creating inventory items
- Retrieving item details
- Listing all items
- Updating item quantity or thresholds
- Deleting items
- Listing low-stock items for restocking

Role:
- Admin
"""

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app.db.models.inventory import Inventory
from app.schemas.inventory import InventoryItemCreate, InventoryItemUpdate, InventoryItemRead


# --- Helper for InventoryItemRead instantiation ---
def _build_inventory_read(inventory):
    return InventoryItemRead(
        id=inventory.id,
        item_name=inventory.item_name,
        quantity=inventory.quantity,
        unit=inventory.unit,
        reorder_level=inventory.reorder_level,
        created_at=inventory.created_at,
        updated_at=inventory.updated_at,
        category=inventory.category,
        supplier_id=inventory.supplier_id,
        cost_per_unit=inventory.cost_per_unit,
        expiry_date=inventory.expiry_date,
        storage_location=inventory.storage_location,
        audit_notes=inventory.audit_notes,
        is_active=getattr(inventory, 'is_active', True),
        last_restocked_at=getattr(inventory, 'last_restocked_at', None),
        last_used_at=getattr(inventory, 'last_used_at', None),
        total_restocks=getattr(inventory, 'total_restocks', 0),
        total_usage=getattr(inventory, 'total_usage', 0),
        average_usage_per_day=getattr(inventory, 'average_usage_per_day', 0.0),
        days_until_restock=getattr(inventory, 'days_until_restock', None),
        days_until_expiry=getattr(inventory, 'days_until_expiry', None),
        low_stock_warning=getattr(inventory, 'low_stock_warning', False),
        last_audit_date=getattr(inventory, 'last_audit_date', None),
        restaurant_id=inventory.restaurant_id
    )


async def create_inventory_item(db: AsyncSession, item_data: InventoryItemCreate, restaurant_id: int) -> InventoryItemRead:
    """
    Create a new inventory item for a restaurant. Role: Admin
    """
    data = item_data.dict(exclude_unset=True)
    data_filtered = {k: v for k, v in data.items() if k in Inventory.__table__.columns.keys()}
    data_filtered["restaurant_id"] = restaurant_id
    # Accept item_name directly from the schema, do not expect 'name'
    # Remove the line that tries to pop 'name' and assign it to 'item_name'
    data_filtered["reorder_level"] = data_filtered.pop("threshold", 10) if "threshold" in data_filtered else data_filtered.get("reorder_level", 10)
    inventory = Inventory(**data_filtered)
    db.add(inventory)
    await db.commit()
    await db.refresh(inventory)
    return _build_inventory_read(inventory)


async def get_inventory_item(db: AsyncSession, item_id: int) -> InventoryItemRead:
    """
    Retrieve a specific inventory item by ID. Role: Admin
    """
    result = await db.execute(select(Inventory).where(Inventory.id == item_id))
    inventory = result.scalars().first()
    if not inventory:
        raise Exception("Inventory item not found")
    return _build_inventory_read(inventory)


async def list_inventory_items(db: AsyncSession, restaurant_id: int) -> List[InventoryItemRead]:
    """
    List all inventory items for a restaurant. Role: Admin
    """
    result = await db.execute(select(Inventory).where(Inventory.restaurant_id == restaurant_id))
    inventories = result.scalars().all()
    return [_build_inventory_read(inv) for inv in inventories]


async def update_inventory_item(db: AsyncSession, item_id: int, item_data: InventoryItemUpdate) -> InventoryItemRead:
    """
    Update an existing inventory item’s data. Role: Admin
    """
    result = await db.execute(select(Inventory).where(Inventory.id == item_id))
    inventory = result.scalars().first()
    if not inventory:
        raise Exception("Inventory item not found")
    update_data = item_data.dict(exclude_unset=True)
    if "name" in update_data:
        inventory.item_name = update_data.pop("name")
    if "threshold" in update_data:
        inventory.reorder_level = update_data.pop("threshold")
    for key, value in update_data.items():
        if hasattr(inventory, key):
            setattr(inventory, key, value)
    await db.commit()
    await db.refresh(inventory)
    return _build_inventory_read(inventory)


async def delete_inventory_item(db: AsyncSession, item_id: int) -> dict:
    """
    Delete an inventory item by its ID. Role: Admin
    """
    result = await db.execute(select(Inventory).where(Inventory.id == item_id))
    inventory = result.scalars().first()
    if not inventory:
        raise Exception("Inventory item not found")
    await db.delete(inventory)
    await db.commit()
    return {"detail": "Inventory item deleted successfully"}


async def list_low_stock_items(db: AsyncSession, restaurant_id: int, threshold: Optional[int] = None) -> List[InventoryItemRead]:
    """
    Retrieve inventory items with quantity below a threshold. Role: Admin
    """
    if threshold is None:
        result = await db.execute(select(Inventory).where(Inventory.restaurant_id == restaurant_id, Inventory.quantity < Inventory.reorder_level))
    else:
        result = await db.execute(select(Inventory).where(Inventory.restaurant_id == restaurant_id, Inventory.quantity < threshold))
    inventories = result.scalars().all()
    return [_build_inventory_read(inv) for inv in inventories]
