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

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import notification_service


async def send_reservation_reminder_controller(
    reservation_id: int,
    db: AsyncSession = Depends(),
    current_user = Depends()
):
    """
    Sends a reminder email to the user for a specific reservation.
    Role: User
    """
    try:
        await notification_service.send_reservation_reminder(reservation_id, db)
        return {"message": "Reservation reminder sent."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def send_order_confirmation_controller(
    order_id: int,
    db: AsyncSession = Depends(),
    current_user = Depends()
):
    """
    Sends an order confirmation email to the user.
    Role: User
    """
    try:
        await notification_service.send_order_confirmation(order_id, db)
        return {"message": "Order confirmation sent."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def send_order_receipt_controller(
    order_id: int,
    db: AsyncSession = Depends(),
    current_user = Depends()
):
    """
    Sends an order receipt email to the user.
    Role: User
    """
    try:
        await notification_service.send_order_receipt(order_id, db)
        return {"message": "Order receipt sent."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def send_admin_alert_controller(
    message: str,
    subject: str = "Admin Notification",
    db: AsyncSession = Depends(),
    current_user = Depends()
):
    """
    Sends a broadcast alert to all admin users.
    Role: Admin
    """
    try:
        await notification_service.send_admin_notification(message, subject, db)
        return {"message": "Admin alert sent."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
