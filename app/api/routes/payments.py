"""
Payment processing API routes.

Handles payment initiation, verification, status retrieval, and webhook callbacks.
Supports integration with multiple payment gateways (e.g., Stripe, Paymob).
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.payment import PaymentInitiate, PaymentStatus, PaymentConfirm
from app.api.deps import get_current_user, get_db
from app.controllers import payment_controller

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/", response_model=dict)
async def initiate_payment(
    payment_data: PaymentInitiate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Initiate a new payment session.
    Role: User
    """
    try:
        return await payment_controller.initiate_payment_controller(payment_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{payment_id}", response_model=dict)
async def get_payment_status(
    payment_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve the status of an existing payment.
    Role: User
    """
    try:
        return await payment_controller.get_payment_status_controller(payment_id, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/{payment_id}/confirm", response_model=dict)
async def confirm_payment(
    payment_id: int,
    confirmation_data: PaymentConfirm,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Confirm a payment after front-end processing.
    Role: User
    """
    try:
        return await payment_controller.confirm_payment_controller(payment_id, confirmation_data, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/webhook", response_model=dict)
async def payment_webhook(request: Request):
    """
    Handle incoming payment gateway webhooks.
    Role: Public
    """
    try:
        return await payment_controller.payment_webhook_controller(request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
