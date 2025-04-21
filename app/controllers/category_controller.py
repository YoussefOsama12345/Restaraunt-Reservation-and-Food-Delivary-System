"""
Category Controller

Handles requests related to food category operations like creation, retrieval,
update, and deletion. Delegates business logic to the `category_service`.
"""

from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session


# Role : Admin
def create_category(
    category_data,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Create a new food category.

    Role: Admin
    """
    pass


def list_categories(
    db: Session = Depends()
):
    """
    Retrieve all food categories.

    Role: Public
    """
    pass


def get_category_by_id(
    category_id: int,
    db: Session = Depends()
):
    """
    Retrieve a single category by its ID.

    Role: Public
    """
    pass


# Role : Admin
def update_category(
    category_id: int,
    update_data,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Update an existing category's information.

    Role: Admin
    """
    pass


# Role : Admin
def delete_category(
    category_id: int,
    db: Session = Depends(),
    current_user: Depends = Depends()
):
    """
    Delete a category by its ID.

    Role: Admin
    """
    pass
