"""
Support Ticket Controller

Manages customer support ticket interactions including creation,
retrieval, updating status, posting replies, and deletion.
Delegates logic to support_service.
"""

from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session


def create_support_ticket_controller(
    ticket_data: Depends,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> Depends:
    """
    Create a new support ticket related to an order or reservation.
    Role: User
    """
    pass


def get_support_ticket_controller(
    ticket_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> Depends:
    """
    Get full details for a single ticket, including messages and status.
    Role: User
    """
    pass


def list_support_tickets_by_user_controller(
    user_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> List[Depends]:
    """
    Get all support tickets submitted by the user.
    Role: User
    """
    pass


def update_ticket_status_controller(
    ticket_id: int,
    new_status: str,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> Depends:
    """
    Update the status of a support ticket.
    Role: User or Admin
    """
    pass


def reply_to_ticket_controller(
    ticket_id: int,
    reply_data: Depends,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> Depends:
    """
    Append a reply to the conversation thread of a support ticket.
    Role: User
    """
    pass


def close_ticket_controller(
    ticket_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends(),
) -> dict:
    """
    Close a support ticket and optionally archive it.
    Role: User
    """
    pass
