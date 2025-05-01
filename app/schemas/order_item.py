from pydantic import BaseModel
from typing import Optional

class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    special_instructions: Optional[str] = None

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    special_instructions: Optional[str] = None

class OrderItemRead(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
