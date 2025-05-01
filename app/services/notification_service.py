"""
Notification Service

Handles email notifications for events such as:
- Reservation reminders
- Order confirmations and receipts
- Admin alerts

Each function simulates interaction with user and order data.
"""

from app.services.email_service import send_email
from app.services.user_service import get_user_by_id
from app.services.order_service import get_order
from app.services.reservation_service import get_reservation
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.models.order import Order
from app.db.models.reservation import Reservation
from app.db.database import get_db
from sqlalchemy.future import select

async def send_reservation_reminder(reservation_id: int, db: AsyncSession = None) -> None:
    """
    Send a reservation reminder email to the user 30 minutes before their reservation.
    Args:
        reservation_id (int): ID of the reservation to remind.
    Role: User
    """
    if db is None:
        raise Exception("Database session required")
    result = await db.execute(select(Reservation).where(Reservation.id == reservation_id))
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise Exception("Reservation not found")
    result = await db.execute(select(User).where(User.id == reservation.user_id))
    user = result.scalar_one_or_none()
    if not user or not user.email:
        raise Exception("User for reservation not found or has no email")
    subject = "Reservation Reminder"
    # Use reservation.reservation_date (datetime or date) and format as needed
    # If reservation_date is a datetime, extract date and time
    if hasattr(reservation, 'reservation_date'):
        reservation_dt = reservation.reservation_date
        if hasattr(reservation_dt, 'strftime'):
            date_str = reservation_dt.strftime('%Y-%m-%d')
            time_str = reservation_dt.strftime('%H:%M')
        else:
            date_str = str(reservation_dt)
            time_str = ''
    else:
        date_str = ''
        time_str = ''
    body = f"Dear {user.email},\n\nThis is a reminder for your reservation on {date_str} at {time_str}.\n\nThank you!"
    send_email(user.email, subject, body)

async def send_order_confirmation(order_id: int, db: AsyncSession = None) -> None:
    """
    Send an order confirmation email immediately after order placement.
    Args:
        order_id (int): ID of the order to confirm.
    Role: User
    """
    if db is None:
        raise Exception("Database session required")
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise Exception("Order not found")
    result = await db.execute(select(User).where(User.id == order.user_id))
    user = result.scalar_one_or_none()
    if not user or not user.email:
        raise Exception("User for order not found or has no email")
    subject = "Order Confirmation"
    body = f"Dear {user.email},\n\nYour order #{order.id} has been placed successfully.\n\nThank you for ordering!"
    send_email(user.email, subject, body)

async def send_order_receipt(order_id: int, db: AsyncSession = None) -> None:
    """
    Send an order receipt email with a link to the receipt PDF.
    Args:
        order_id (int): ID of the order to send receipt for.
    Role: User
    """
    if db is None:
        raise Exception("Database session required")
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise Exception("Order not found")
    result = await db.execute(select(User).where(User.id == order.user_id))
    user = result.scalar_one_or_none()
    if not user or not user.email:
        raise Exception("User for order not found or has no email")
    subject = "Order Receipt"
    body = f"Dear {user.email},\n\nHere is your receipt for order #{order.id}.\n\n[Download Receipt](https://yourdomain.com/receipts/{order.id})\n\nThank you!"
    send_email(user.email, subject, body)

async def send_admin_notification(message: str, subject: str = "Admin Notification", db: AsyncSession = None) -> None:
    """
    Send a notification email to all admin users.
    Args:
        message (str): The notification content.
        subject (str): Email subject line.
    Role: Admin
    """
    if db is None:
        raise Exception("Database session required")
    result = await db.execute(select(User).where(User.role == "admin"))
    admins = result.scalars().all()
    if not admins:
        raise Exception("No admin users found")
    for admin in admins:
        if admin.email:
            send_email(admin.email, subject, message)
