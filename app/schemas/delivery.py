from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

class DeliveryStatusEnum(str, Enum):
    ASSIGNED = "assigned"
    EN_ROUTE = "en_route"
    DELIVERED = "delivered"
    FAILED = "failed"

class DeliveryBase(BaseModel):
    order_id: int
    delivery_address: str
    delivery_fee: float
    delivery_instructions: Optional[str] = None
    
class DeliveryCreate(DeliveryBase):
    customer_id: int
    restaurant_id: int
    
class DeliveryAssign(BaseModel):
    driver_id: int
    
class DeliveryUpdate(BaseModel):
    status: Optional[DeliveryStatusEnum] = None
    pickup_time: Optional[datetime] = None
    delivery_time: Optional[datetime] = None
    estimated_delivery_time: Optional[datetime] = None
    actual_delivery_time: Optional[datetime] = None
    vehicle_type: Optional[str] = None
    priority_level: Optional[str] = None
    distance_km: Optional[float] = None
    location_latitude: Optional[float] = None
    location_longitude: Optional[float] = None
    
class DeliveryComplete(BaseModel):
    status: DeliveryStatusEnum = DeliveryStatusEnum.DELIVERED
    actual_delivery_time: datetime
    
class DeliveryRead(DeliveryBase):
    id: int
    driver_id: Optional[int] = None
    customer_id: int
    restaurant_id: int
    status: DeliveryStatusEnum
    pickup_time: Optional[datetime] = None
    delivery_time: Optional[datetime] = None
    estimated_delivery_time: Optional[datetime] = None
    actual_delivery_time: Optional[datetime] = None
    delivery_instructions: Optional[str] = None
    vehicle_type: Optional[str] = None
    priority_level: Optional[str] = None
    distance_km: Optional[float] = None
    rating: Optional[int] = None
    feedback: Optional[str] = None
    location_latitude: Optional[float] = None
    location_longitude: Optional[float] = None
    
    class Config:
        orm_mode = True
