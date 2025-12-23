from pydantic import BaseModel, Field
from typing import Optional, List

from serializers.user import UserResponseSchema
# from serializers.session import SessionSchema  

class InstructorSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str

    # Relationships
    user: Optional[UserResponseSchema] = None  
    # Sessions: List[SessionSchema] = []  

    class Config:
        orm_mode = True  

class InstructorCreateSchema(BaseModel):
    name: str
