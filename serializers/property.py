from pydantic import BaseModel, Field
from typing import Optional, List
from .review import ReviewSchema
from .user import UserResponseSchema


class PropertySchema(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    price: int
    numOfRooms: int
    numOfBathrooms: int
    location: str


    reviews: List[ReviewSchema] = []
    user: UserResponseSchema

    class Config:
        orm_mode = True


class PropertyCreateSchema(BaseModel):
        title: str
        price: int
        numOfRooms: int
        numOfBathrooms: int
        location: str 



