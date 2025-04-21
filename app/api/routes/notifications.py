"""
Notification API Routes

This module defines API endpoints for sending notifications to users and admins:
- Reservation reminders
- Order confirmations
- Order receipts
- Admin broadcast alerts

All endpoints require authentication.
"""
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/notifications", tags=["notifications"])


def reservation_reminder(reservation_id: int, current_user):
    """
    Send a reminder email for a reservation.
    Role: User
    """
    pass


def order_confirmation(order_id: int, current_user):
    """
    Send an email confirmation after order placement.
    Role: User
    """
    pass


def order_receipt(order_id: int, current_user):
    """
    Send a receipt email for an order.
    Role: User
    """
    pass


def notify_admins(message: str, current_user, subject: str = "Admin Notification"):
    """
    Send a custom alert to all admin users.
    Role: Admin
    """
    pass
