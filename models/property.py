from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class PropertyModel(BaseModel):

    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    numOfRooms = Column(Integer)
    numOfBathrooms = Column(Integer)
    location = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


    user = relationship('UserModel', back_populates='properties')
    # reviews = relationship('ReviewModel', back_populates='property')  
