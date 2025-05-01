"""
Delivery Task Controller

Manages delivery task operations for drivers and admins.
Handles assigning deliveries, updating delivery status, and confirming delivery completion.
Delegates core logic to the delivery_service module.
"""

from app.services.delivary_task_service import assign_delivery, get_assigned_deliveries as get_assigned_deliveries_service, update_delivery_status as update_delivery_status_service, confirm_delivery_with_otp
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


async def get_assigned_deliveries(
    driver_id: int,
    db: AsyncSession,
    current_user
):
    """
    Retrieve deliveries assigned to a specific driver.

    Role: Driver
    """
    # Optionally, check current_user.role == 'driver' and current_user.id == driver_id
    return await get_assigned_deliveries_service(db, driver_id)


async def assign_delivery_task(
    order_id: int,
    driver_id: int,
    db: AsyncSession,
    current_user
):
    """
    Assign an order to a delivery driver.

    Role: Admin
    """
    # Optionally, check current_user.role == 'admin'
    return await assign_delivery(db, order_id, driver_id)


async def update_delivery_status(
    task_id: int,
    status: str,
    db: AsyncSession,
    current_user
):
    """
    Update the status of a delivery task.

    Role: Driver or Admin
    """
    # Check if user is admin or the assigned driver
    if current_user.role == "admin":
        # Admins can update any delivery task
        print(f"Admin user {current_user.id} updating delivery task {task_id}")
        # Pass 0 as driver_id to bypass driver check in service
        return await update_delivery_status_service(db, task_id, status, 0, is_admin=True)
    else:
        # Regular drivers can only update their own tasks
        print(f"Driver {current_user.id} updating delivery task {task_id}")
        return await update_delivery_status_service(db, task_id, status, current_user.id, is_admin=False)


async def confirm_delivery_otp(
    task_id: int,
    otp: str,
    db: AsyncSession,
    current_user
):
    """
    Confirm delivery completion using OTP.

    Role: Driver or Admin
    """
    # Check if user is admin or the assigned driver
    if current_user.role == "admin":
        # Admins can confirm any delivery task
        print(f"Admin user {current_user.id} confirming delivery task {task_id}")
        # Pass 0 as driver_id to bypass driver check in service
        return await confirm_delivery_with_otp(db, task_id, otp, 0, is_admin=True)
    else:
        # Regular drivers can only confirm their own tasks
        print(f"Driver {current_user.id} confirming delivery task {task_id}")
        return await confirm_delivery_with_otp(db, task_id, otp, current_user.id, is_admin=False)
