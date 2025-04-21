"""
Notification Service

Handles email notifications for events such as:
- Reservation reminders
- Order confirmations and receipts
- Admin alerts

Each function simulates interaction with user and order data.
"""

from datetime import timedelta


def send_reservation_reminder(reservation_id: int) -> None:
    """
    Send a reservation reminder email to the user 30 minutes before their reservation.

    Args:
        reservation_id (int): ID of the reservation to remind.

    Role: User
    """
    pass


def send_order_confirmation(order_id: int) -> None:
    """
    Send an order confirmation email immediately after order placement.

    Args:
        order_id (int): ID of the order to confirm.

    Role: User
    """
    pass


def send_order_receipt(order_id: int) -> None:
    """
    Send an order receipt email with a link to the receipt PDF.

    Args:
        order_id (int): ID of the order to send receipt for.

    Role: User
    """
    pass


def send_admin_notification(message: str, subject: str = "Admin Notification") -> None:
    """
    Send a notification email to all admin users.

    Args:
        message (str): The notification content.
        subject (str): Email subject line.

    Role: Admin
    """
    pass
