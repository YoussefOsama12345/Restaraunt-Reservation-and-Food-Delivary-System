"""
Discount Module

This module defines the `Discount` model for the Restaurant Management System (RMS).
The `Discount` class represents discounts that can be applied to orders, such as promotional 
or seasonal discounts. Each discount is associated with a unique code, a percentage value, 
and a validity period.

Models:
-------
- Discount: Represents a discount available for orders, including attributes like discount code, 
    percentage, and validity dates.

Usage:
------
This model is used to manage the discounts applied to customer orders in the RMS. Discounts 
could be applied to the total order amount, either as a fixed amount or a percentage.
"""

from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from database.base import Base
from sqlalchemy.orm import relationship

class Discount(Base):
    """
    Discount model represents discounts available for orders, such as promotional or seasonal discounts.
    """
    __tablename__ = "discounts"

    def __repr__(self):
        return f"<Discount(code={self.code}, percentage={self.percentage})>"