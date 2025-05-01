from datetime import datetime
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.db.models.delivery_task import DeliveryTask, DeliveryStatus
from app.db.models.order import Order
from app.db.models.user import User, UserRole

async def create_delivery_task(delivery_data: dict, db: AsyncSession) -> dict:
    """
    Create a new delivery task for an order.
    
    Args:
        delivery_data (dict): Delivery task data including order_id.
        db (AsyncSession): Database session.
        
    Returns:
        dict: Created delivery task data.
    """
    try:
        # Check if order exists
        order_result = await db.execute(select(Order).where(Order.id == delivery_data["order_id"]))
        order = order_result.scalars().first()
        if not order:
            raise ValueError(f"Order with ID {delivery_data['order_id']} not found")
            
        # Create delivery task
        delivery_task = DeliveryTask(**delivery_data)
        db.add(delivery_task)
        await db.flush()
        
        # Get delivery task ID
        await db.refresh(delivery_task)
        
        # Create result dictionary
        result = {c.name: getattr(delivery_task, c.name) for c in DeliveryTask.__table__.columns}
        
        # Add timestamp information manually since they don't exist in the database yet
        current_time = datetime.utcnow().isoformat()
        result['created_at'] = current_time
        result['updated_at'] = current_time
        
        await db.commit()
        return result
    except Exception as e:
        await db.rollback()
        raise ValueError(f"Failed to create delivery task: {str(e)}")

async def assign_driver(delivery_id: int, driver_id: int, db: AsyncSession) -> dict:
    """
    Assign a driver to a delivery task.
    
    Args:
        delivery_id (int): ID of the delivery task.
        driver_id (int): ID of the driver to assign.
        db (AsyncSession): Database session.
        
    Returns:
        dict: Updated delivery task data.
    """
    try:
        # Check if delivery task exists
        delivery_result = await db.execute(select(DeliveryTask).where(DeliveryTask.id == delivery_id))
        delivery_task = delivery_result.scalars().first()
        if not delivery_task:
            raise ValueError(f"Delivery task with ID {delivery_id} not found")
            
        # Check if driver exists and has driver role
        driver_result = await db.execute(select(User).where(User.id == driver_id))
        driver = driver_result.scalars().first()
        if not driver:
            raise ValueError(f"User with ID {driver_id} not found")
        if driver.role != UserRole.DRIVER:
            raise ValueError(f"User with ID {driver_id} is not a driver")
            
        # Assign driver to delivery task
        delivery_task.driver_id = driver_id
        delivery_task.status = DeliveryStatus.ASSIGNED
        # Note: updated_at field is removed as it doesn't exist in the database yet
        
        await db.commit()
        await db.refresh(delivery_task)
        
        # Create result dictionary
        result = {c.name: getattr(delivery_task, c.name) for c in DeliveryTask.__table__.columns}
        
        # Add timestamp information manually since they don't exist in the database yet
        current_time = datetime.utcnow().isoformat()
        result['created_at'] = current_time
        result['updated_at'] = current_time
        
        return result
    except Exception as e:
        await db.rollback()
        raise ValueError(f"Failed to assign driver: {str(e)}")

async def update_delivery_status(delivery_id: int, status_data: dict, db: AsyncSession) -> dict:
    """
    Update the status of a delivery task.
    
    Args:
        delivery_id (int): ID of the delivery task.
        status_data (dict): Status data including status, location, etc.
        db (AsyncSession): Database session.
        
    Returns:
        dict: Updated delivery task data.
    """
    try:
        # Check if delivery task exists
        delivery_result = await db.execute(select(DeliveryTask).where(DeliveryTask.id == delivery_id))
        delivery_task = delivery_result.scalars().first()
        if not delivery_task:
            raise ValueError(f"Delivery task with ID {delivery_id} not found")
            
        # Update delivery task fields
        for field, value in status_data.items():
            if hasattr(delivery_task, field) and field in DeliveryTask.__table__.columns.keys():
                setattr(delivery_task, field, value)
                
        # Update timestamps based on status
        # Note: updated_at field is removed as it doesn't exist in the database yet
        if status_data.get("status") == DeliveryStatus.EN_ROUTE and not delivery_task.pickup_time:
            delivery_task.pickup_time = datetime.utcnow()
        elif status_data.get("status") == DeliveryStatus.DELIVERED and not delivery_task.actual_delivery_time:
            delivery_task.actual_delivery_time = datetime.utcnow()
            delivery_task.delivery_time = datetime.utcnow()
            
        await db.commit()
        await db.refresh(delivery_task)
        
        # Create result dictionary
        result = {c.name: getattr(delivery_task, c.name) for c in DeliveryTask.__table__.columns}
        
        # Add timestamp information manually since they don't exist in the database yet
        current_time = datetime.utcnow().isoformat()
        result['created_at'] = current_time
        result['updated_at'] = current_time
        
        return result
    except Exception as e:
        await db.rollback()
        raise ValueError(f"Failed to update delivery status: {str(e)}")

async def get_delivery_task(delivery_id: int, db: AsyncSession) -> dict:
    """
    Get a delivery task by ID.
    
    Args:
        delivery_id (int): ID of the delivery task.
        db (AsyncSession): Database session.
        
    Returns:
        dict: Delivery task data.
    """
    try:
        # Get delivery task with driver and order
        delivery_result = await db.execute(
            select(DeliveryTask)
            .options(joinedload(DeliveryTask.driver), joinedload(DeliveryTask.order))
            .where(DeliveryTask.id == delivery_id)
        )
        delivery_task = delivery_result.scalars().first()
        if not delivery_task:
            raise ValueError(f"Delivery task with ID {delivery_id} not found")
            
        # Create result dictionary
        result = {c.name: getattr(delivery_task, c.name) for c in DeliveryTask.__table__.columns}
        
        # Add timestamp information manually since they don't exist in the database yet
        current_time = datetime.utcnow().isoformat()
        result['created_at'] = current_time
        result['updated_at'] = current_time
        
        # Add driver info if available
        if delivery_task.driver:
            result["driver_name"] = delivery_task.driver.full_name
            result["driver_phone"] = delivery_task.driver.phone_number
            
        return result
    except Exception as e:
        raise ValueError(f"Failed to get delivery task: {str(e)}")

async def get_driver_deliveries(driver_id: int, db: AsyncSession) -> list:
    """
    Get all delivery tasks assigned to a driver.
    
    Args:
        driver_id (int): ID of the driver.
        db (AsyncSession): Database session.
        
    Returns:
        list: List of delivery task data.
    """
    try:
        # Check if driver exists and has driver role
        driver_result = await db.execute(select(User).where(User.id == driver_id))
        driver = driver_result.scalars().first()
        if not driver:
            raise ValueError(f"User with ID {driver_id} not found")
        if driver.role != UserRole.DRIVER:
            raise ValueError(f"User with ID {driver_id} is not a driver")
            
        # Get all delivery tasks assigned to driver
        delivery_result = await db.execute(
            select(DeliveryTask)
            .options(joinedload(DeliveryTask.order))
            .where(DeliveryTask.driver_id == driver_id)
        )
        delivery_tasks = delivery_result.scalars().all()
        
        # Create result list
        result = []
        for task in delivery_tasks:
            task_dict = {c.name: getattr(task, c.name) for c in DeliveryTask.__table__.columns}
            
            # Add timestamp information manually since they don't exist in the database yet
            current_time = datetime.utcnow().isoformat()
            task_dict['created_at'] = current_time
            task_dict['updated_at'] = current_time
            
            result.append(task_dict)
            
        return result
    except Exception as e:
        raise ValueError(f"Failed to get driver deliveries: {str(e)}")

async def get_available_drivers(db: AsyncSession) -> list:
    """
    Get all available drivers.
    
    Args:
        db (AsyncSession): Database session.
        
    Returns:
        list: List of driver data.
    """
    try:
        # Get all users with driver role
        driver_result = await db.execute(select(User).where(User.role == UserRole.DRIVER))
        drivers = driver_result.scalars().all()
        
        # Create result list
        result = []
        for driver in drivers:
            driver_dict = {
                "id": driver.id,
                "full_name": driver.full_name,
                "username": driver.username,
                "email": driver.email,
                "phone_number": driver.phone_number
            }
            result.append(driver_dict)
            
        return result
    except Exception as e:
        raise ValueError(f"Failed to get available drivers: {str(e)}")
