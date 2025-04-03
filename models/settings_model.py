"""
Settings Model

This module defines the `Settings` model, which stores global configuration for the Restaurant Management System (RMS).
It allows the system to store and retrieve configurable settings, such as operational parameters, tax rates, and other
system-wide configurations that may change over time.

The `Settings` model can be used to store values that can be dynamically modified without needing to change the codebase, 
providing flexibility in system configuration.
"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from datetime import datetime

class Settings(Base):
    """
    Settings model stores global configuration for the Restaurant Management System (RMS),
    including system-wide parameters that can be adjusted without modifying the codebase.
    """
    __tablename__ = "settings"

    def __repr__(self):
        return f"<Setting(key={self.key}, value={self.value})>"