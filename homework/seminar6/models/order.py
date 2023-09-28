from pydantic import BaseModel, Field
from datetime import datetime

class Order(BaseModel):
    id: int = Field(...)
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    order_date: datetime = Field(default=datetime.utcnow())
    order_status: bool = Field(default=False)


class OrderIn(BaseModel):
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    order_date: datetime = Field(default=datetime.utcnow())
    order_status: bool = Field(default=False)
