"""
models/notification.py

Defines the SQLAlchemy ORM model for in-app notifications.

This model represents messages sent to users for updates, alerts, promotions,
or system-related events. It supports categorization, read tracking, metadata,
archiving, and expiration logic.

Classes:
    - Notification: SQLAlchemy model representing a single user notification.

Usage:
    Notifications are used in user dashboards, real-time alerts,
    push messages, and email summaries.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Notification(Base):
    """
    Notification model representing messages sent to users.

    Attributes:
        - id: Primary key
        - user_id: FK to the receiving user
        - title: Brief title or subject of the notification
        - message: Full content of the notification
        - is_read: Boolean flag indicating if the user has read the notification
        - created_at: Timestamp when the notification was created
        - type: Category of notification (e.g., system, promo, warning)
        - priority: Importance level (low, medium, high)
        - action_url: Optional link associated with the notification
        - notification_metadata: Optional JSON string storing extra details
        - expires_at: Expiration timestamp for temporary notifications
        - tags: Optional comma-separated tags (e.g., "order,offer")
        - archived: Whether the notification was archived by the user
        - archived_at: Timestamp of when it was archived
        - read_at: Timestamp of when the user read the notification

    Relationships:
        - user: Link to the receiving User
    """
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(String(50), default="general")
    priority = Column(String(20), default="medium")
    action_url = Column(String(255), nullable=True)
    notification_metadata = Column(Text, nullable=True)  # JSON string
    expires_at = Column(DateTime, nullable=True)
    tags = Column(String(255), nullable=True)
    archived = Column(Boolean, default=False)
    archived_at = Column(DateTime, nullable=True)
    read_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="notifications")
