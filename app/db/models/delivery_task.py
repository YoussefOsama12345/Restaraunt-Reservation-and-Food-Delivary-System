"""
models/delivery_task.py

Defines the SQLAlchemy ORM model for DeliveryTask entities.

Each DeliveryTask represents a delivery operation linked to an order.
It captures the full life cycle of a delivery — from assignment to completion — 
including timing, driver info, vehicle type, delivery fee, feedback, and geolocation.

Classes:
    - DeliveryStatus: Enum for allowed delivery task states
    - DeliveryTask: SQLAlchemy model representing a food delivery assignment

Usage:
    Used in logistics tracking, driver assignment systems, ETA calculations,
    and delivery analytics.
"""

from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    Column, Integer, String, Float, Text, DateTime, ForeignKey, Enum
)
from sqlalchemy.orm import relationship
from .base import Base


class DeliveryStatus(str, PyEnum):
    """Enumeration of valid delivery statuses."""
    ASSIGNED = "assigned"
    EN_ROUTE = "en_route"
    DELIVERED = "delivered"
    FAILED = "failed"


class DeliveryTask(Base):
    """
    DeliveryTask model representing the delivery workflow of an order.

    Attributes:
        - id: Primary key
        - order_id: FK to the order being delivered
        - driver_id: FK to the assigned delivery person (nullable)
        - customer_id: FK to the end user receiving the order
        - restaurant_id: FK to the source restaurant
        - delivery_address: Full delivery address in text
        - status: Current task status (assigned, en_route, etc.)
        - pickup_time: When the order was picked up by the driver
        - delivery_time: When the order was delivered
        - estimated_delivery_time: Predicted delivery window
        - actual_delivery_time: Confirmed delivery timestamp
        - delivery_instructions: Notes from the customer or restaurant
        - vehicle_type: Type of transport used (bike, car, etc.)
        - priority_level: Delivery urgency level (low, medium, high)
        - distance_km: Distance of delivery route
        - delivery_fee: Fee charged for this delivery
        - rating: Customer rating for this delivery
        - feedback: Optional review text
        - location_latitude: Last known latitude (for tracking)
        - location_longitude: Last known longitude

    Relationships:
        - order: One-to-one link to the related Order
        - driver: Many-to-one link to the assigned delivery person (User)
    """
    __tablename__ = "delivery_tasks"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    delivery_address = Column(Text, nullable=False)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.ASSIGNED)
    pickup_time = Column(DateTime, nullable=True)
    delivery_time = Column(DateTime, nullable=True)
    estimated_delivery_time = Column(DateTime, nullable=True)
    actual_delivery_time = Column(DateTime, nullable=True)
    delivery_instructions = Column(Text, nullable=True)
    vehicle_type = Column(String(20), nullable=True)
    priority_level = Column(String(20), default="medium")
    distance_km = Column(Float, nullable=True)
    delivery_fee = Column(Float, nullable=False)
    rating = Column(Integer, nullable=True)
    feedback = Column(Text, nullable=True)
    location_latitude = Column(Float, nullable=True)
    location_longitude = Column(Float, nullable=True)

    # Relationships
    order = relationship("Order", back_populates="delivery_task")
    driver = relationship("User", back_populates="delivery_tasks")
