"""
Inventory Module

This module defines the `Inventory` model for the Restaurant Management System (RMS).
The `Inventory` class stores details about ingredients, products, and other items available
in the restaurant's inventory, including their names, quantities, prices, and other relevant
information for efficient stock management.

Models:
-------
- Inventory: Represents items in the restaurant's inventory such as ingredients or products,
    including attributes like item name, quantity, price, and expiration date.

Usage:
------
The `Inventory` model is used to track and manage inventory items in the RMS. This includes 
adding, updating, and querying the stock of ingredients and products available for orders.
"""

from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime
from database.base import Base

class Inventory(Base):
    """
    Inventory model stores details about ingredients, products, and other items available in the restaurant's inventory.
    """
    __tablename__ = "inventory"

    pass

    def __repr__(self):
        return f"<Inventory(item_id={self.item_id}, name={self.name}, quantity={self.quantity})>"