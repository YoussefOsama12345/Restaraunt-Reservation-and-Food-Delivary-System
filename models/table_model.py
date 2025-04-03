"""
Table Module

This module defines the `Table` model for the Restaurant Management System (RMS).
The `Table` model represents the dining tables in the restaurant, including details
such as table number, capacity, and availability status.

Models:
-------
- Table: Represents a dining table in the restaurant, including its unique identifier, table number, capacity, 
    and availability status.

Usage:
------
The `Table` model is used to manage and track tables in the restaurant, including their availability for
reservations, seating capacity, and table-specific details.
"""

from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database.base import Base

class Table(Base):
    """
    Table model represents a dining table in the restaurant, including its capacity and availability status.
    """
    __tablename__ = "tables"

    def __repr__(self):
        return f"<Table(table_id={self.table_id}, table_number={self.table_number})>"
