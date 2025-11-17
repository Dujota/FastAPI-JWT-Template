from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel

class RequestModel(BaseModel):

    __tablename__ = "request"

    id = Column(Integer, primary_key=True, index=True)

    # Columens For Request Table
    title = Column(String)
    approval = Column(Boolean)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('user.id'))
    property_id = Column(Integer, ForeignKey('property.id'))

    # Relationships
    user = relationship('UserModel', back_populates="requests")
    property = relationship('PropertyModel', back_populates="request")



