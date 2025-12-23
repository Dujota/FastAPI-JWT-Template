
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship
from .base import BaseModel
from datetime import datetime  


class GymClassModel(BaseModel):
    __tablename__ = "gym_classes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("CategoryModel", back_populates="gym_classes")
