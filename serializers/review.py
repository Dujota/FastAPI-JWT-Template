from pydantic import BaseModel, Field
from typing import Optional

class ReviewSchema(BaseModel):
  id: Optional[int] = Field(default=None)
  content: str

  class Config:
    orm_mode = True