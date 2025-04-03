"""
Supplier Module

This module defines the `Supplier` model for the Restaurant Management System (RMS).
The `Supplier` model stores details about the suppliers providing ingredients, products,
and other goods to the restaurant.

Models:
-------
- Supplier: Represents a supplier providing goods and services to the restaurant.

Usage:
------
The `Supplier` model is used to manage and track supplier information, such as contact 
details, supplied items, and other related information.
"""

from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from database.base import Base

class Supplier(Base):
    """
    Supplier model represents suppliers providing ingredients and other goods to the restaurant.
    """
    __tablename__ = "suppliers"


    def __repr__(self):
        return f"<Supplier(name={self.name}, supplier_id={self.supplier_id})>"
