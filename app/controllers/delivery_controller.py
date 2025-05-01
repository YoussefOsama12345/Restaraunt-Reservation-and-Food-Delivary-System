from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services import delivery_service
from app.api.deps import get_current_user
from app.schemas.delivery import DeliveryCreate, DeliveryAssign, DeliveryUpdate, DeliveryComplete

async def create_delivery_controller(delivery_data: DeliveryCreate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> dict:
    """
    Controller for creating a new delivery task.
    """
    try:
        # Convert Pydantic model to dict using .dict() (Pydantic v1 compatibility)
        delivery_dict = delivery_data.dict()
        
        # Create delivery task
        result = await delivery_service.create_delivery_task(delivery_dict, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def assign_driver_controller(delivery_id: int, assignment_data: DeliveryAssign, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> dict:
    """
    Controller for assigning a driver to a delivery task.
    """
    try:
        # Convert Pydantic model to dict using .dict() (Pydantic v1 compatibility)
        driver_id = assignment_data.dict()["driver_id"]
        
        # Assign driver
        result = await delivery_service.assign_driver(delivery_id, driver_id, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def update_delivery_status_controller(delivery_id: int, status_data: DeliveryUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> dict:
    """
    Controller for updating the status of a delivery task.
    """
    try:
        # Convert Pydantic model to dict using .dict() (Pydantic v1 compatibility)
        status_dict = status_data.dict(exclude_unset=True)
        
        # Update delivery status
        result = await delivery_service.update_delivery_status(delivery_id, status_dict, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def complete_delivery_controller(delivery_id: int, completion_data: DeliveryComplete, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> dict:
    """
    Controller for completing a delivery task.
    """
    try:
        # Convert Pydantic model to dict using .dict() (Pydantic v1 compatibility)
        completion_dict = completion_data.dict()
        
        # Update delivery status to completed
        result = await delivery_service.update_delivery_status(delivery_id, completion_dict, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def get_delivery_controller(delivery_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> dict:
    """
    Controller for getting a delivery task by ID.
    """
    try:
        result = await delivery_service.get_delivery_task(delivery_id, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def get_driver_deliveries_controller(driver_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> list:
    """
    Controller for getting all delivery tasks assigned to a driver.
    """
    try:
        result = await delivery_service.get_driver_deliveries(driver_id, db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def get_available_drivers_controller(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)) -> list:
    """
    Controller for getting all available drivers.
    """
    try:
        result = await delivery_service.get_available_drivers(db)
        return result
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
