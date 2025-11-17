from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class ReviewModel(BaseModel):
    __tablename__ = 'reviews'

    #primary key for each review
    id = Column(Integer, primary_key=True, index=True)

    content = Column(String, nullable=False)

    #relationship
    review_id = Column(String, nullable = False)
    review = relationship("ReviewModel", back_populates="reviews")

