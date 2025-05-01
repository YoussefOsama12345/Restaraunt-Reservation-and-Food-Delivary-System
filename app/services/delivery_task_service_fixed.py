"""
Delivery Task Service

Handles logic for assigning and managing delivery tasks:

- Assigning orders to delivery drivers
- Retrieving assigned deliveries
- Updating delivery status (en route, delivered, failed)
- Confirming delivery with OTP or proof

Roles:
- Admin (assign deliveries)
- Driver (view, update, confirm)
"""

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from app.db.models.delivery_task import DeliveryTask, DeliveryStatus
from app.db.models.order import Order
from app.db.models.user import User
from app.schemas.delivery_task import DeliveryCreate, DeliveryUpdateStatus, DeliveryRead
from fastapi import HTTPException
from datetime import datetime

async def assign_delivery(db: AsyncSession, order_id: int, driver_id: int) -> dict:
    """
    Assign an order to a delivery driver.
    Role: Admin
    """
    try:
        # Check if order exists
        order_result = await db.execute(select(Order).where(Order.id == order_id))
        order = order_result.scalar_one_or_none()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found.")
            
        # Get delivery address in a separate query
        address_id = None
        delivery_address = "Address not available"
        
        # First try to get the address_id directly from the order
        try:
            address_id_result = await db.execute(
                select(Order.delivery_address_id).where(Order.id == order_id)
            )
            address_id = address_id_result.scalar_one_or_none()
        except Exception as e:
            print(f"Could not get address_id: {str(e)}")
            
        # If we have an address_id, try to get the address details
        if address_id:
            try:
                # Get address details in a separate query to avoid greenlet error
                address_query = "SELECT street_address, city, state, postal_code, country FROM addresses WHERE id = :address_id"
                address_result = await db.execute(address_query, {"address_id": address_id})
                address_row = address_result.fetchone()
                
                if address_row:
                    # Construct address string from components
                    address_parts = []
                    if address_row[0]:  # street_address
                        address_parts.append(address_row[0])
                    if address_row[1]:  # city
                        address_parts.append(address_row[1])
                    if address_row[2]:  # state
                        address_parts.append(address_row[2])
                    if address_row[3]:  # postal_code
                        address_parts.append(address_row[3])
                    if address_row[4]:  # country
                        address_parts.append(address_row[4])
                        
                    delivery_address = ", ".join(address_parts)
            except Exception as e:
                print(f"Could not get address details: {str(e)}")
                
        # Check if driver exists and is a driver
        driver_result = await db.execute(select(User).where(User.id == driver_id, User.role == "driver"))
        driver = driver_result.scalar_one_or_none()
        if not driver:
            raise HTTPException(status_code=404, detail="Driver not found or not a driver.")
            
        # Check if delivery task already exists for this order
        existing_result = await db.execute(select(DeliveryTask).where(DeliveryTask.order_id == order_id))
        existing = existing_result.scalar_one_or_none()
        if existing:
            # Instead of raising an error, return the existing task with detailed information
            # Convert SQLAlchemy model to dict with proper datetime handling
            task_dict = {}
            for c in DeliveryTask.__table__.columns:
                value = getattr(existing, c.name)
                # Handle datetime objects properly
                if isinstance(value, datetime):
                    task_dict[c.name] = value.isoformat()
                else:
                    task_dict[c.name] = value
            
            # Add timestamp information manually since they don't exist in the database yet
            current_time = datetime.utcnow().isoformat()
            task_dict['created_at'] = current_time
            task_dict['updated_at'] = current_time
            
            # Add driver information as extra data
            driver_info_result = await db.execute(
                select(User.id, User.username, User.full_name, User.phone_number)
                .where(User.id == existing.driver_id)
            )
            driver_info = driver_info_result.fetchone()
            if driver_info:
                task_dict["driver_details"] = {
                    "id": driver_info[0],
                    "username": driver_info[1],
                    "full_name": driver_info[2],
                    "phone_number": driver_info[3]
                }
            
            # Add order information as extra data
            order_info_result = await db.execute(
                select(Order.id, Order.status, Order.total_amount)
                .where(Order.id == existing.order_id)
            )
            order_info = order_info_result.fetchone()
            if order_info:
                task_dict["order_details"] = {
                    "id": order_info[0],
                    "status": order_info[1],
                    "total_amount": order_info[2]
                }
                
            return task_dict
            
        # Create delivery task with safe address handling
        delivery_task = DeliveryTask(
            order_id=order_id,
            driver_id=driver_id,
            customer_id=order.user_id,
            restaurant_id=order.restaurant_id,
            delivery_address=delivery_address,
            status=DeliveryStatus.ASSIGNED,
            delivery_fee=4.99  # Example: could be dynamic
            # Note: created_at and updated_at fields are not included
            # as they don't exist in the database yet
        )
        db.add(delivery_task)
        await db.commit()
        await db.refresh(delivery_task)
        
        # Convert to dictionary with proper datetime handling
        task_dict = {}
        for c in DeliveryTask.__table__.columns:
            value = getattr(delivery_task, c.name)
            # Handle datetime objects properly
            if isinstance(value, datetime):
                task_dict[c.name] = value.isoformat()
            else:
                task_dict[c.name] = value
        
        # Add timestamp information manually since they don't exist in the database yet
        current_time = datetime.utcnow().isoformat()
        task_dict['created_at'] = current_time
        task_dict['updated_at'] = current_time
        
        # Add driver information as extra data
        driver_info_result = await db.execute(
            select(User.id, User.username, User.full_name, User.phone_number)
            .where(User.id == driver_id)
        )
        driver_info = driver_info_result.fetchone()
        if driver_info:
            task_dict["driver_details"] = {
                "id": driver_info[0],
                "username": driver_info[1],
                "full_name": driver_info[2],
                "phone_number": driver_info[3]
            }
        
        # Add order information as extra data
        order_info_result = await db.execute(
            select(Order.id, Order.status, Order.total_amount)
            .where(Order.id == order_id)
        )
        order_info = order_info_result.fetchone()
        if order_info:
            task_dict["order_details"] = {
                "id": order_info[0],
                "status": order_info[1],
                "total_amount": order_info[2]
            }
            
        return task_dict
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise e
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to assign delivery: {str(e)}")

async def update_delivery_status(db: AsyncSession, task_id: int, status: str, driver_id: int) -> dict:
    """
    Update the status of a delivery task.
    Role: Driver or Admin
    """
    try:
        # Check if delivery task exists and belongs to the driver
        task_result = await db.execute(
            select(DeliveryTask).where(
                DeliveryTask.id == task_id,
                DeliveryTask.driver_id == driver_id
            )
        )
        task = task_result.scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Delivery task not found or not assigned to this driver.")
            
        # Update status and related fields
        if status == DeliveryStatus.EN_ROUTE and not task.pickup_time:
            task.pickup_time = datetime.utcnow()
        elif status == DeliveryStatus.DELIVERED and not task.actual_delivery_time:
            task.actual_delivery_time = datetime.utcnow()
            task.delivery_time = datetime.utcnow()
            
            # Update order status to delivered
            order_result = await db.execute(select(Order).where(Order.id == task.order_id))
            order = order_result.scalar_one_or_none()
            if order:
                order.status = "delivered"
                order.actual_delivery_time = datetime.utcnow()
                
        # Update task status
        task.status = status
        
        await db.commit()
        await db.refresh(task)
        
        # Convert to dictionary
        task_dict = {}
        for c in DeliveryTask.__table__.columns:
            value = getattr(task, c.name)
            if isinstance(value, datetime):
                task_dict[c.name] = value.isoformat()
            else:
                task_dict[c.name] = value
                
        # Add timestamp information manually
        current_time = datetime.utcnow().isoformat()
        task_dict['updated_at'] = current_time
        if 'created_at' not in task_dict or task_dict['created_at'] is None:
            task_dict['created_at'] = current_time
                
        return task_dict
    except HTTPException as e:
        raise e
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update delivery status: {str(e)}")

async def confirm_delivery_with_otp(db: AsyncSession, task_id: int, otp: str, driver_id: int) -> dict:
    """
    Confirm the delivery completion using OTP verification.
    Role: Driver or Admin
    """
    try:
        # Check if delivery task exists and belongs to the driver
        task_result = await db.execute(
            select(DeliveryTask).where(
                DeliveryTask.id == task_id,
                DeliveryTask.driver_id == driver_id
            )
        )
        task = task_result.scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Delivery task not found or not assigned to this driver.")
            
        # In a real application, we would verify the OTP here
        # For this example, we'll just accept any OTP
        if not otp:
            raise HTTPException(status_code=400, detail="OTP is required.")
            
        # Update task status to delivered
        task.status = DeliveryStatus.DELIVERED
        task.actual_delivery_time = datetime.utcnow()
        task.delivery_time = datetime.utcnow()
        
        # Update order status to delivered
        order_result = await db.execute(select(Order).where(Order.id == task.order_id))
        order = order_result.scalar_one_or_none()
        if order:
            order.status = "delivered"
            order.actual_delivery_time = datetime.utcnow()
            
        await db.commit()
        await db.refresh(task)
        
        # Convert to dictionary
        task_dict = {}
        for c in DeliveryTask.__table__.columns:
            value = getattr(task, c.name)
            if isinstance(value, datetime):
                task_dict[c.name] = value.isoformat()
            else:
                task_dict[c.name] = value
                
        # Add timestamp information manually
        current_time = datetime.utcnow().isoformat()
        task_dict['updated_at'] = current_time
        if 'created_at' not in task_dict or task_dict['created_at'] is None:
            task_dict['created_at'] = current_time
                
        return task_dict
    except HTTPException as e:
        raise e
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to confirm delivery: {str(e)}")
