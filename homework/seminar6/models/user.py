from pydantic import Field, BaseModel


class User(BaseModel):
    id: int = Field(...)
    firstname: str = Field(..., max_length=32)
    lastname: str = Field(..., max_length=32)
    email: str = Field(..., max_length=64)
    password: str = Field(..., max_length=64)
    isActive: bool = Field(default=True)


class UserIn(BaseModel):
    firstname: str = Field(..., max_length=32)
    lastname: str = Field(..., max_length=32)
    email: str = Field(..., max_length=64)
    password: str = Field(..., max_length=64)
    isActive: bool = Field(default=True)
