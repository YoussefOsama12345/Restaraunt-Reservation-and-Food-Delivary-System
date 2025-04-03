"""
Staff Module

This module defines the `Staff` model for the Restaurant Management System (RMS).
The `Staff` model stores details about the restaurant's employees, such as their names, 
roles, shift timings, and salary.

Models:
-------
- Staff: Represents an employee working at the restaurant, with details about their role,
    working hours, and compensation.

Usage:
------
The `Staff` model is used to manage and track employee information, such as assigning roles, 
monitoring shifts, and managing payroll.
"""

from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime
from database.base import Base

class Staff(Base):
    """
    Staff model represents employees working at the restaurant,
    including details like name, role, shift, and salary.
    """
    __tablename__ = "staff"

    def __repr__(self):
        return f"<Staff(name={self.name}, staff_id={self.staff_id}, role={self.role})>"
