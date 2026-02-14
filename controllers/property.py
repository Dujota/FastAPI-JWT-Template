from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.property import PropertyModel
from models.user import UserModel
from serializers.property import PropertySchema, PropertyCreate as PropertyCreateShcema

from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user


router = APIRouter()

@router.get('/properties', response_model=List[PropertySchema])
def get_properties(db: Session = Depends(get_db)):
    properties = db.query(PropertyModel).all()
    return properties


@router.get('/properties/{property_id}', response_model=PropertySchema)
def get_single_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first()
    
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    
    return property


@router.post('/properties' , response_model=PropertySchema)
def create_property(property: PropertyCreateShcema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_property = PropertyModel(**property.dict(), user_id = current_user.id)
    
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    
    return new_property

@router.put('/properties/{property_id}', response_model=PropertySchema)
def update_property(property_id: int, property: PropertyCreateShcema, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first()
    
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    
    if db_property.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    property_data = property.dict(exclude_unset=True)
    
    for key, value in property_data.items():
        setattr(db_property, key, value)
        
    db.commit()
    db.refresh(db_property)
    
    return db_property


@router.delete('/properties/{property_id}')
def delete_property(property_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first()
    
    if not db_property:
        raise HTTPException(status_code=404, detail="property not found")
    
    if db_property.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    db.delete(db_property)
    db.commit()
    
    return {"message": f"Tea with ID {property_id} has been deleted"}
