from pydantic import BaseModel, Field
from typing import Optional, List
from serializers.gymclass import gymclassSchema

class CategorySchema(BaseModel):
    id: Optional[int] = Field(default=None) # This makes sure you don't have to explicitly add an id when sending json data
    name: str
    description: str
    gym_classes: List[gymclassSchema] = []

    # sessions: List[SessionSchema] = []

class CategoryCreateSchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True