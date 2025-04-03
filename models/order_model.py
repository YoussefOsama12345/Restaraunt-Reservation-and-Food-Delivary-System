"""
Order Module

This module defines the `Order` model for the Restaurant Management System (RMS).
The `Order` model stores details about customer orders, including information about
the items ordered, prices, discounts, and the total amount. Each order is associated 
with a customer and contains references to the ordered items, payment details, and discounts.

Models:
-------
- Order: Represents an order placed by a customer, including the total amount, associated 
    menu items, discounts, and customer details.

Usage:
------
The `Order` model is used to manage customer orders in the RMS. It is essential for tracking 
and processing customer orders, calculating totals, and applying discounts.
"""


from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class Order(Base):
    """
    Order model stores details of customer orders, including items ordered, prices, and associated discounts.
    """
    __tablename__ = "orders"

    def __repr__(self):
        return f"<Order(order_id={self.order_id}, total_amount={self.total_amount})>"