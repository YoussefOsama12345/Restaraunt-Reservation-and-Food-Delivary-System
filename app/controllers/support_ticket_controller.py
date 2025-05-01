"""
Support Ticket Controller

Manages customer support ticket interactions including creation,
retrieval, updating status, posting replies, and deletion.
Delegates logic to support_service.
"""

from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import support_service
from app.schemas.support_ticket import SupportTicketCreate, SupportTicketUpdate, SupportTicketRead


async def create_support_ticket_controller(
    ticket_data: SupportTicketCreate,
    current_user,
    db: AsyncSession = Depends(),
) -> SupportTicketRead:
    """
    Create a new support ticket related to an order or reservation.
    Role: User
    """
    try:
        ticket_dict = ticket_data.dict()
        result = await support_service.create_support_ticket(ticket_dict, current_user, db)
        return SupportTicketRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def get_support_ticket_controller(
    ticket_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> SupportTicketRead:
    """
    Get full details for a single ticket, including messages and status.
    Role: User
    """
    try:
        result = await support_service.get_support_ticket(ticket_id, db)
        return SupportTicketRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


async def list_support_tickets_by_user_controller(
    user_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> List[SupportTicketRead]:
    """
    Get all support tickets submitted by the user.
    Role: User
    """
    try:
        results = await support_service.list_support_tickets_by_user(user_id, current_user, db)
        return [SupportTicketRead(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def update_ticket_status_controller(
    ticket_id: int,
    new_status: str,
    current_user,
    db: AsyncSession = Depends(),
) -> SupportTicketRead:
    """
    Update the status of a support ticket.
    Role: User or Admin
    """
    try:
        update_dict = {"status": new_status}
        result = await support_service.update_support_ticket(ticket_id, update_dict, current_user, db)
        return SupportTicketRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def reply_to_ticket_controller(
    ticket_id: int,
    reply_data: SupportTicketUpdate,
    current_user,
    db: AsyncSession = Depends(),
) -> SupportTicketRead:
    """
    Append a reply to the conversation thread of a support ticket.
    Role: User
    """
    try:
        update_dict = reply_data.dict(exclude_unset=True)
        result = await support_service.update_support_ticket(ticket_id, update_dict, current_user, db)
        return SupportTicketRead(**result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


async def close_ticket_controller(
    ticket_id: int,
    current_user,
    db: AsyncSession = Depends(),
) -> dict:
    """
    Close a support ticket and optionally archive it.
    Role: User
    """
    try:
        return await support_service.delete_support_ticket(ticket_id, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
