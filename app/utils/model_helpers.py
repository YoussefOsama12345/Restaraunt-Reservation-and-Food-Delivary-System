"""
Utility functions for model conversion and validation.
"""

from datetime import datetime
from typing import Dict, Any

def prepare_user_data_for_pydantic(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Prepare user data from database for Pydantic model validation.
    Ensures all required fields have proper values.
    
    Args:
        user_data: Dictionary with user data from database
        
    Returns:
        Dictionary with prepared user data
    """
    # Make a copy to avoid modifying the original
    prepared_data = user_data.copy()
    
    # Handle datetime fields
    if prepared_data.get("created_at") is None:
        prepared_data["created_at"] = datetime(1970, 1, 1)
    if prepared_data.get("updated_at") is None:
        prepared_data["updated_at"] = datetime(1970, 1, 1)
        
    # Ensure boolean fields are not None
    if prepared_data.get("is_active") is None:
        prepared_data["is_active"] = True
    if prepared_data.get("is_admin") is None:
        prepared_data["is_admin"] = False
        
    # Ensure other required fields have default values
    if prepared_data.get("orders_count") is None:
        prepared_data["orders_count"] = 0
    if prepared_data.get("reservations_count") is None:
        prepared_data["reservations_count"] = 0
    if prepared_data.get("total_spent") is None:
        prepared_data["total_spent"] = 0.0
    if prepared_data.get("account_status") is None:
        prepared_data["account_status"] = "active"
    if prepared_data.get("verification_status") is None:
        prepared_data["verification_status"] = "unverified"
        
    return prepared_data
