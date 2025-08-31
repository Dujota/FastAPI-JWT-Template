from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel
# from .session import SessionModel



class InstructorModel(BaseModel):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))


    # Relationships : 
    user = relationship('UserModel', back_populates='instructors')
    # Sessions = relationship('SessionModel', back_populates='instructors')
