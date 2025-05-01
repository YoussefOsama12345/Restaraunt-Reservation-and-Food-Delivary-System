"""
Support ticket API routes.

Allows users to submit support tickets, view their ticket history,
and allows admin users to respond or change ticket status.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.support_ticket import SupportTicketCreate, SupportTicketUpdate, SupportTicketRead
from app.api.deps import get_current_user, get_db
from app.controllers import support_ticket_controller

router = APIRouter(prefix="/support", tags=["support"])


@router.post("/", response_model=SupportTicketRead)
async def create_ticket(
    ticket_data: SupportTicketCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Submit a new support ticket.
    Role: User
    """
    try:
        return await support_ticket_controller.create_support_ticket_controller(ticket_data, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/my", response_model=List[SupportTicketRead])
async def list_user_tickets(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Retrieve all tickets submitted by the authenticated user.
    Role: User
    """
    return await support_ticket_controller.list_support_tickets_by_user_controller(current_user.id, current_user, db)


@router.get("/all", response_model=List[SupportTicketRead])
async def list_all_tickets(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Admin-only endpoint to list all submitted support tickets.
    Role: Admin
    """
    # TODO: Add admin check logic here
    return await support_ticket_controller.list_support_tickets_by_user_controller(current_user.id, current_user, db)


@router.get("/{ticket_id}", response_model=SupportTicketRead)
async def get_ticket(
    ticket_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get details of a specific support ticket by its ID.
    Role: User
    """
    try:
        return await support_ticket_controller.get_support_ticket_controller(ticket_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{ticket_id}", response_model=SupportTicketRead)
async def update_ticket(
    ticket_id: int,
    update_data: SupportTicketUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Admin-only endpoint to update the status or reply of a ticket.
    Role: Admin
    """
    # TODO: Add admin check logic here
    try:
        return await support_ticket_controller.update_ticket_status_controller(ticket_id, update_data.status, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
