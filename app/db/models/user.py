"""
models/user.py

This module defines the SQLAlchemy ORM model for the User entity, including user roles 
and associated metadata, relationships, and lifecycle attributes. It is a core component 
of the user management system within the application.

Overview:
    - Provides a comprehensive structure for storing user-related data.
    - Supports role-based access control using the `UserRole` enum.
    - Maintains timestamps for user activity (creation, update, last login).
    - Tracks user engagement (orders, reservations, payments).
    - Establishes rich relationship mappings to other entities for full relational context.

Classes:
    - UserRole: Enumeration of possible user roles in the system. Defines user permissions and access levels.
        * CUSTOMER: Regular user who interacts with the app as a client.
        * ADMIN: System administrator with elevated privileges.
        * DRIVER: Delivery personnel responsible for order fulfillment.

    - User: Declarative SQLAlchemy model for representing application users.
        * Fields include personal information, authentication data, activity metrics, and status flags.
        * Relationships are declared for associated entities like orders, reviews, addresses, etc.

Usage:
    This model is integral to authentication, authorization, profile management,
    and user analytics. It serves as a parent for one-to-many relationships to other models
    such as Order, Reservation, Payment, SupportTicket, and more.

Example:
    >>> new_user = User(
            email="example@example.com",
            hashed_password=hash_function("securepassword"),
            username="user123",
            role=UserRole.CUSTOMER
        )

Notes:
    - Ensure indexes on frequently queried fields such as email and username.
    - Default values are used for fields like account status and verification to ensure consistency.
"""


from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from .base import Base


class UserRole(str, PyEnum):
    """
    Enumeration for defining roles of users in the system.
    """
    CUSTOMER = "customer"
    ADMIN = "admin"
    DRIVER = "driver"

class User(Base):
    """
    User model representing application users.

    Attributes:
        - id: Primary key
        - email: Unique email address
        - hashed_password: Securely hashed user password
        - full_name: Full name of the user
        - phone_number: Optional contact number
        - is_active: Boolean status of account
        - role: Enum representing user role (Customer, Admin, Driver)
        - created_at: Timestamp for user creation
        - updated_at: Timestamp for last update
        - username: Unique username
        - account_status: Status string (active, suspended, etc.)
        - verification_status: Email/account verification status
        - orders_count: Number of orders made
        - reservations_count: Number of reservations made
        - total_spent: Total money spent
        - average_rating: User's average review rating
        - last_login: Timestamp of last login

    Relationships:
        - addresses: One-to-many with Address
        - orders: One-to-many with Order
        - reservations: One-to-many with Reservation
        - reviews: One-to-many with Review
        - support_tickets: One-to-many with SupportTicket
        - payments: One-to-many with Payment
        - notifications: One-to-many with Notification
        - cart_items: One-to-many with CartItem
        - assigned_deliveries: Orders assigned to the user as delivery person
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    username = Column(String(50), unique=True, nullable=False)
    account_status = Column(String(20), default="active")
    verification_status = Column(String(20), default="unverified")
    orders_count = Column(Integer, default=0)
    reservations_count = Column(Integer, default=0) 
    total_spent = Column(Float, default=0.0)
    average_rating = Column(Float, nullable=True)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan", foreign_keys="Order.user_id")
    assigned_deliveries = relationship("Order", foreign_keys="Order.delivery_person_id")
    reservations = relationship("Reservation", back_populates="user", cascade="all, delete-orphan", foreign_keys="Reservation.user_id")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    support_tickets = relationship("SupportTicket", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="user", cascade="all, delete-orphan")
    # delivery_tasks = relationship("DeliveryTask", back_populates="driver", cascade="all, delete-orphan", foreign_keys="DeliveryTask.driver_id")  # REMOVED: No delivery_tasks property on User
