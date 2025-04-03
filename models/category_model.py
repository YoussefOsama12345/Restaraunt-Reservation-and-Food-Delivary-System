"""
Category Module

This module defines the `Category` model for the Restaurant Management System (RMS).
The `Category` class represents the different categories of menu items, such as Appetizers,
Main Courses, Desserts, etc. Each category is associated with multiple menu items in the system.

Models:
-------
- Category: Represents a category of menu items (e.g., Appetizers, Main Courses, Desserts).
"""


from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base


class Category(Base):
    """
    Category model represents different categories of menu items (e.g., Appetizers, Main Courses, Desserts).
    """
    __tablename__ = "categories"

    def __repr__(self):
        return f"<Category(name={self.name}, category_id={self.category_id})>"