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
from sqlalchemy.orm import Session
from typing import List

# Placeholder models and schemas
class SupportTicket:
    id: int
    user_id: int
    status: str
    subject: str
    description: str

class SupportTicketCreate:
    subject: str
    description: str

class SupportTicketUpdate:
    status: str

class SupportReplyCreate:
    message: str


def create_support_ticket(ticket_data: SupportTicketCreate, user_id: int) -> SupportTicket:
    """
    Submit a new support ticket.
    Role: User
    """
    pass


def get_support_ticket(ticket_id: int, user_id: int, is_admin: bool = False) -> SupportTicket:
    """
    Retrieve a specific support ticket by ID.
    Role: User (own), Admin (any)
    """
    pass


def list_support_tickets_by_user(user_id: int) -> List[SupportTicket]:
    """
    List all support tickets submitted by a specific user.
    Role: User
    """
    pass


def list_all_support_tickets() -> List[SupportTicket]:
    """
    List all support tickets in the system.
    Role: Admin
    """
    pass


def update_ticket_status(ticket_id: int, status: str, admin_id: int) -> SupportTicket:
    """
    Update the status of a support ticket.
    Role: Admin
    """
    pass


def reply_to_ticket(ticket_id: int, reply_data: SupportReplyCreate, user_id: int) -> SupportTicket:
    """
    Reply to a support ticket.
    Role: User
    """
    pass
