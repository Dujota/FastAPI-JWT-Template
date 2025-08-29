from typing import Optional, List
from pydantic import BaseModel, Field
from .user import UserResponseSchema
from .property import PropertySchema

class RequestSchema(BaseModel):
   id: Optional[int] = Field(default=None)
   title: str
   approval: bool

   # Relationships
   user: UserResponseSchema
   property: List[PropertySchema]

   class Config:
      orm_mode = True