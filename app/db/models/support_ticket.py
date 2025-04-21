"""
models/support_ticket.py

Defines the SQLAlchemy ORM model for support tickets submitted by users.

Each support ticket captures user issues, priorities, assigned agents, 
and resolution metrics. It facilitates customer service workflows such as
status tracking, response handling, and satisfaction monitoring.

Classes:
    - SupportTicket: SQLAlchemy model representing a user's support inquiry.

Usage:
    Used in admin dashboards, customer support systems, and feedback analytics.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from .base import Base


class SupportTicket(Base):
    """
    SupportTicket model representing a customer support issue submitted by a user.

    Attributes:
        - id: Primary key
        - user_id: FK to the user who submitted the ticket
        - subject: Short subject line of the support request
        - description: Detailed description of the problem or inquiry
        - status: Current ticket status (open, in_progress, resolved, closed)
        - priority: Importance level (low, medium, high)
        - created_at: Timestamp when the ticket was created
        - updated_at: Timestamp of the last update
        - assigned_to: Optional name or ID of the support agent handling the ticket
        - response_count: Number of replies from support
        - resolution_time: Time taken to resolve the issue (in minutes/hours)
        - customer_satisfaction: Rating provided by the user after resolution
        - last_response_at: Timestamp of the last support response

    Relationships:
        - user: Reference to the User who created the support ticket
    """
    __tablename__ = "support_tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(20), default="open")  # open, in_progress, resolved, closed
    priority = Column(String(20), default="medium")  # low, medium, high
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    assigned_to = Column(String(100), nullable=True)
    response_count = Column(Integer, default=0)
    resolution_time = Column(Integer, nullable=True)
    customer_satisfaction = Column(Integer, nullable=True)
    last_response_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="support_tickets")
