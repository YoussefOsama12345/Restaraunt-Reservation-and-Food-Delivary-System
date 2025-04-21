"""
Category Service

Handles business logic related to food menu categories.

Includes:
- Creating new categories
- Retrieving individual category details
- Listing all categories
- Updating category information
- Deleting a category

Roles:
- Admin: Create, update, delete
- Public: List and retrieve
"""

from typing import List, Optional
from sqlalchemy.orm import Session
# Placeholder models and schemas
class Category:
    id: int
    name: str
    description: str

class CategoryCreate:
    name: str
    description: str

class CategoryUpdate:
    name: Optional[str]
    description: Optional[str]


def create_category(category_data: CategoryCreate) -> Category:
    """
    Create a new menu category.
    Role: Admin
    """
    pass


def get_category(category_id: int) -> Category:
    """
    Retrieve a category by its ID.
    Role: Public
    """
    pass


def list_categories() -> List[Category]:
    """
    Retrieve a list of all categories.
    Role: Public
    """
    pass


def update_category(category_id: int, update_data: CategoryUpdate) -> Category:
    """
    Update an existing category.
    Role: Admin
    """
    pass


def delete_category(category_id: int) -> dict:
    """
    Delete a category by its ID.
    Role: Admin
    """
    pass
