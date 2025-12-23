from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.gymclass import GymClassModel
from models.user import UserModel
from serializers.category import gymclassSchema, gymclassCreateSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()


# GET all gym classes

@router.get("/gymclasses", response_model=List[gymclassSchema])
def get_gym_classes(db: Session = Depends(get_db)):
    gym_classes = db.query(GymClassModel).all()
    return gym_classes

# GET single gym class

@router.get("/gymclasses/{gymclass_id}", response_model=gymclassSchema)
def get_single_gym_class(gymclass_id: int, db: Session = Depends(get_db)):
    gym_class = db.query(GymClassModel).filter(GymClassModel.id == gymclass_id).first()
    if not gym_class:
        raise HTTPException(status_code=404, detail="Gym class not found")
    return gym_class


# CREATE gym class (admin only)

@router.post("/gymclasses", response_model=gymclassSchema)
def create_gym_class(
    gym_class_data: gymclassCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create gym classes")

    new_gym_class = GymClassModel(**gym_class_data.dict())
    db.add(new_gym_class)
    db.commit()
    db.refresh(new_gym_class)
    return new_gym_class


# UPDATE gym class (admin only)

@router.put("/gymclasses/{gymclass_id}", response_model=gymclassSchema)
def update_gym_class(
    gymclass_id: int,
    gym_class_data: gymclassCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    db_gym_class = db.query(GymClassModel).filter(GymClassModel.id == gymclass_id).first()
    if not db_gym_class:
        raise HTTPException(status_code=404, detail="Gym class not found")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can update gym classes")

    data = gym_class_data.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_gym_class, key, value)

    db.commit()
    db.refresh(db_gym_class)
    return db_gym_class


# DELETE gym class (admin only)

@router.delete("/gymclasses/{gymclass_id}")
def delete_gym_class(
    gymclass_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    db_gym_class = db.query(GymClassModel).filter(GymClassModel.id == gymclass_id).first()
    if not db_gym_class:
        raise HTTPException(status_code=404, detail="Gym class not found")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can delete gym classes")

    db.delete(db_gym_class)
    db.commit()
    return {"message": f"Gym class with ID {gymclass_id} has been deleted"}
