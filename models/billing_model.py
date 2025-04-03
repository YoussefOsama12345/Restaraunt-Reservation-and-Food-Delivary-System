"""
Billing Module

This module defines the Billing model for the Restaurant Management System (RMS).
The `Billing` class represents a record of a customer's bill, capturing key details 
such as the total amount billed, the payment method used, and the associated reservation.

The `Billing` model is part of the database schema and is used for tracking payments 
and generating invoices for customer reservations. It includes attributes such as the 
total amount, payment method, and the foreign key referencing the associated reservation.
"""

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class Billing(Base):
    """
    Billing model stores details about customer bills,
    including the total amount, payment method, and associated reservation.
    """
    __tablename__ = "billing"

    def __repr__(self):
        return f"<Billing(bill_id={self.bill_id}, total_amount={self.total_amount})>"
