"""
models/inventory.py

Defines the SQLAlchemy ORM model for inventory tracking at restaurants.

Each inventory record tracks item quantities, stock levels, cost, expiry,
usage, and audit information. This model supports advanced restaurant
supply management including reordering, spoilage, and supplier metrics.

Classes:
    - Inventory: SQLAlchemy model representing an inventory item for a restaurant.

Usage:
    Used for restaurant inventory dashboards, automated stock alerts,
    and backend analytics for restocking and cost optimization.
"""

from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .base import Base


class Inventory(Base):
    """
    Inventory model representing stock and supply data for a restaurant.

    Attributes:
        - id: Primary key
        - restaurant_id: FK to the restaurant that owns the inventory
        - item_name: Name of the inventory item
        - quantity: Current quantity in stock
        - unit: Measurement unit (e.g., kg, liters, pieces)
        - reorder_level: Threshold below which reordering is needed
        - category: Optional item category (e.g., dairy, beverage)
        - supplier_id: Optional reference to supplier (if applicable)
        - cost_per_unit: Cost of each unit for financial tracking
        - expiry_date: Expiration date for perishable items
        - storage_location: Text description of where item is stored
        - total_restocks: Number of times the item was restocked
        - total_usage: Total amount of item used
        - average_usage_per_day: Daily usage rate for forecasting
        - low_stock_warning: Boolean flag indicating low stock status
        - last_audit_date: Timestamp of last manual or system audit
        - audit_notes: Optional notes from the last audit
        - created_at: Timestamp of creation
        - updated_at: Timestamp of last update

    Relationships:
        - restaurant: Link to the Restaurant owning the inventory
    """
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    item_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=False)  # kg, liters, pieces, etc.
    reorder_level = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category = Column(String(50), nullable=True)
    supplier_id = Column(Integer, nullable=True)
    cost_per_unit = Column(Float, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    storage_location = Column(String(100), nullable=True)
    total_restocks = Column(Integer, default=0)
    total_usage = Column(Integer, default=0)
    average_usage_per_day = Column(Float, default=0.0)
    low_stock_warning = Column(Boolean, default=False)
    last_audit_date = Column(DateTime, nullable=True)
    audit_notes = Column(Text, nullable=True)
    
    # Relationships
    restaurant = relationship("Restaurant")
