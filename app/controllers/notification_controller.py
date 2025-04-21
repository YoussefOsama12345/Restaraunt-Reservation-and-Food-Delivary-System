"""
Notification Controller

Handles actions related to sending user and admin notifications, including:
- Reservation reminders
- Order confirmations and receipts
- Admin broadcast alerts

Delegates business logic to the `notification_service` module.

Roles:
- User: Reservation/order notifications
- Admin: Broadcast alerts to other admins
"""

from fastapi import Depends
from sqlalchemy.orm import Session


def send_reservation_reminder_controller(
    reservation_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Sends a reminder email to the user for a specific reservation.
    Role: User
    """
    pass


def send_order_confirmation_controller(
    order_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Sends an order confirmation email to the user.
    Role: User
    """
    pass


def send_order_receipt_controller(
    order_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Sends an order receipt email to the user.
    Role: User
    """
    pass


def send_admin_alert_controller(
    message: str,
    subject: str = "Admin Notification",
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Sends a broadcast alert to all admin users.
    Role: Admin
    """
    pass
