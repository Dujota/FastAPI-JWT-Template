
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class gymclassSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime



class gymclassCreateSchema(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    category_id: int

    class Config:
        orm_mode = True
