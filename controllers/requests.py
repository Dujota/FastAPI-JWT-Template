from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.property import PropertyModel
from models.request import RequestModel
from serializers.request import RequestCreateSchema, RequestSchema
from models.user import UserModel
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user


router = APIRouter()

@router.get('/properties/{property_id}/requests', response_model=List[RequestSchema])
def get_requests(property_id: int,db: Session = Depends(get_db)):
    property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first
    if not property:
        raise HTTPException(status_code=404, detail="Request not found")
    return property.requests

@router.get('/requests/{request_id}', response_model=RequestSchema)
def get_single_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(RequestModel).filter(RequestModel.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

@router.post('/properties/{property_id}/requests', response_model=RequestSchema)
def create_request(request:RequestSchema, db: Session = Depends(get_db)):
    new_request= RequestModel(**request.dict())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request