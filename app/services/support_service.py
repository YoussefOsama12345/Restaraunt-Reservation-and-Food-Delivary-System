"""
Support Service

Handles customer support ticket operations:

- Submitting new support tickets
- Viewing user-specific or individual ticket details
- Updating ticket status
- Replying to tickets (user/agent)
- Deleting/closing tickets

Role:
- User (submit, view own, reply)
- Admin (view all, update status, delete)
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.db.models.support_ticket import SupportTicket
from datetime import datetime
from typing import List, Dict

async def create_support_ticket(ticket_data: dict, current_user, db: AsyncSession) -> dict:
    """
    Submit a new support ticket.
    Role: User
    """
    ticket_fields = {k: v for k, v in ticket_data.items() if k in SupportTicket.__table__.columns.keys()}
    # Map 'message' to 'description' if present
    if 'description' not in ticket_fields or not ticket_fields.get('description'):
        if 'message' in ticket_data and ticket_data['message']:
            ticket_fields['description'] = ticket_data['message']
    ticket_fields['created_at'] = datetime.utcnow()
    ticket_fields['updated_at'] = datetime.utcnow()
    ticket_fields['user_id'] = current_user.id
    ticket = SupportTicket(**ticket_fields)
    db.add(ticket)
    await db.commit()
    await db.refresh(ticket)
    # Always return 'message' in the output for API schema compatibility
    result_dict = {c.name: getattr(ticket, c.name) for c in SupportTicket.__table__.columns}
    result_dict['message'] = result_dict.get('description', '')
    return result_dict

async def get_support_ticket(ticket_id: int, db: AsyncSession) -> dict:
    """
    Retrieve a specific support ticket by ID.
    Role: User (own), Admin (any)
    """
    result = await db.execute(select(SupportTicket).where(SupportTicket.id == ticket_id))
    ticket = result.scalars().first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support ticket not found")
    result_dict = {c.name: getattr(ticket, c.name) for c in SupportTicket.__table__.columns}
    result_dict['message'] = result_dict.get('description', '')
    return result_dict

async def list_support_tickets_by_user(user_id: int, current_user, db: AsyncSession) -> List[dict]:
    """
    List all support tickets submitted by a specific user.
    Role: User
    """
    # Optionally: check if current_user is allowed to view user_id's tickets
    result = await db.execute(select(SupportTicket).where(SupportTicket.user_id == user_id))
    tickets = result.scalars().all()
    output = []
    for t in tickets:
        t_dict = {c.name: getattr(t, c.name) for c in SupportTicket.__table__.columns}
        t_dict['message'] = t_dict.get('description', '')
        output.append(t_dict)
    return output

async def list_all_support_tickets(db: AsyncSession) -> List[dict]:
    """
    List all support tickets in the system.
    Role: Admin
    """
    result = await db.execute(select(SupportTicket))
    tickets = result.scalars().all()
    output = []
    for t in tickets:
        t_dict = {c.name: getattr(t, c.name) for c in SupportTicket.__table__.columns}
        t_dict['message'] = t_dict.get('description', '')
        output.append(t_dict)
    return output

async def update_support_ticket(ticket_id: int, update_data: dict, current_user, db: AsyncSession) -> dict:
    """
    Update the status of a support ticket.
    Role: Admin
    """
    result = await db.execute(select(SupportTicket).where(SupportTicket.id == ticket_id))
    ticket = result.scalars().first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support ticket not found")
    # Check if the user is either the ticket owner or an admin
    if ticket.user_id != current_user.id and current_user.role != "admin":
        print(f"User {current_user.id} with role {current_user.role} tried to update ticket {ticket_id} owned by user {ticket.user_id}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    for field, value in update_data.items():
        if field in SupportTicket.__table__.columns.keys() and value is not None:
            setattr(ticket, field, value)
    ticket.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(ticket)
    result_dict = {c.name: getattr(ticket, c.name) for c in SupportTicket.__table__.columns}
    result_dict['message'] = result_dict.get('description', '')
    return result_dict

async def reply_to_ticket(ticket_id: int, reply_data: dict, user_id: int, db: AsyncSession) -> dict:
    """
    Reply to a support ticket.
    Role: User
    """
    # TO DO: implement reply logic
    pass

async def delete_support_ticket(ticket_id: int, current_user, db: AsyncSession) -> dict:
    """
    Delete a support ticket.
    Role: Admin
    """
    result = await db.execute(select(SupportTicket).where(SupportTicket.id == ticket_id))
    ticket = result.scalars().first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support ticket not found")
    # Check if the user is either the ticket owner or an admin
    if ticket.user_id != current_user.id and current_user.role != "admin":
        print(f"User {current_user.id} with role {current_user.role} tried to update ticket {ticket_id} owned by user {ticket.user_id}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    await db.delete(ticket)
    await db.commit()
    return {"detail": "Support ticket deleted", "id": ticket_id}
