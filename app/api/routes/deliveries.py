"""
Delivery management API routes for drivers.

Provides endpoints for drivers to retrieve assigned deliveries,
assign orders to delivery personnel, update delivery status,
and confirm completion with OTP or proof.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_current_user
from app.schemas.delivery_task import DeliveryRead
from app.controllers import delivery_task_controller

router = APIRouter(
    prefix="",
    tags=["deliveries"]
)

@router.get("/assigned/{driver_id}", response_model=List[DeliveryRead])
async def get_assigned_deliveries(driver_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    return await delivery_task_controller.get_assigned_deliveries(driver_id, db, current_user)

@router.post("/assign", response_model=DeliveryRead, status_code=status.HTTP_201_CREATED)
async def assign_delivery(
    order_id: int = Body(..., description="Order ID to assign for delivery"), 
    driver_id: int = Body(..., description="Driver ID to assign to the delivery"), 
    db: AsyncSession = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    return await delivery_task_controller.assign_delivery_task(order_id, driver_id, db, current_user)

@router.patch("/{task_id}/status", response_model=DeliveryRead)
async def update_delivery_status(task_id: int, status: str, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    return await delivery_task_controller.update_delivery_status(task_id, status, db, current_user)

@router.post("/{task_id}/confirm", status_code=status.HTTP_200_OK)
async def confirm_delivery(task_id: int, otp: str, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    return await delivery_task_controller.confirm_delivery_otp(task_id, otp, db, current_user)
