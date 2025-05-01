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
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.deps import get_current_user, get_db
from app.controllers import notification_controller

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("/reservation-reminder/{reservation_id}")
async def reservation_reminder(
    reservation_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Send a reminder email for a reservation. Role: User
    """
    try:
        return await notification_controller.send_reservation_reminder_controller(reservation_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/order-confirmation/{order_id}")
async def order_confirmation(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Send an email confirmation after order placement. Role: User
    """
    try:
        return await notification_controller.send_order_confirmation_controller(order_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/order-receipt/{order_id}")
async def order_receipt(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Send a receipt email for an order. Role: User
    """
    try:
        return await notification_controller.send_order_receipt_controller(order_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/admin-alert")
async def notify_admins(
    message: str,
    subject: str = "Admin Notification",
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Send a custom alert to all admin users. Role: Admin
    """
    try:
        return await notification_controller.send_admin_alert_controller(message, subject, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
