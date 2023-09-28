from pydantic import Field, BaseModel


class Item(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=64)
    description: str = Field(max_length=256, default='Описание отсутствует')
    price: float = Field(..., ge=100)
    isActive: bool = Field(default=True)


class ItemIn(BaseModel):
    name: str = Field(..., max_length=64)
    description: str = Field(max_length=256, default='Описание отсутствует')
    price: float = Field(..., ge=100)
    isActive: bool = Field(default=True)
