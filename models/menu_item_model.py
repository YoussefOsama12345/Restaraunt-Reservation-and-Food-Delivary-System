"""
MenuItem Module

This module defines the `MenuItem` model for the Restaurant Management System (RMS).
The `MenuItem` class represents a menu item, such as a dish or drink, in the restaurant's 
menu. Each menu item is associated with a specific category (e.g., Appetizers, Main Courses),
allowing the system to organize and display menu items efficiently.

Models:
-------
- MenuItem: Represents a specific item on the restaurant menu, including attributes like 
    name, price, description, category, and availability.

Usage:
------
The `MenuItem` model is used to manage and display menu items in the RMS. This includes 
adding, updating, and querying items in the menu, as well as associating them with a category.
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class MenuItem(Base):
    """
    MenuItem model represents a menu item in the restaurant, such as a specific dish or drink.
    Each menu item is associated with a category (e.g., Appetizer, Main Course).
    """
    __tablename__ = "menu_items"
    

    def __repr__(self):
        return f"<MenuItem(name={self.name}, item_id={self.item_id}, price={self.price})>"