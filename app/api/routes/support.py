"""
Support ticket API routes.

Allows users to submit support tickets, view their ticket history,
and allows admin users to respond or change ticket status.
"""
from fastapi import APIRouter
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/support", tags=["support"])


def create_ticket(ticket_data, current_user):
    """
    Submit a new support ticket.
    Role: User
    """
    pass


def list_user_tickets(current_user):
    """
    Retrieve all tickets submitted by the authenticated user.
    Role: User
    """
    pass


def list_all_tickets(current_user):
    """
    Admin-only endpoint to list all submitted support tickets.
    Role: Admin
    """
    pass


def get_ticket(ticket_id: int, current_user):
    """
    Get details of a specific support ticket by its ID.
    Role: User
    """
    pass


def update_ticket(ticket_id: int, update_data, current_user):
    """
    Admin-only endpoint to update the status or reply of a ticket.
    Role: Admin
    """
    pass
