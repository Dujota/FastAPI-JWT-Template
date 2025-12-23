# categories.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.category import CategoryModel
from models.user import UserModel
from serializers.category import CategorySchema, CategoryCreateSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

# -----------------------
# GET all categories
# -----------------------
@router.get("/categories", response_model=List[CategorySchema])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return categories

# -----------------------
# GET single category
# -----------------------
@router.get("/categories/{category_id}", response_model=CategorySchema)
def get_single_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# -----------------------
# CREATE category (admin only)
# -----------------------
@router.post("/categories", response_model=CategorySchema)
def create_category(
    category: CategoryCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create categories")

    new_category = CategoryModel(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

# -----------------------
# UPDATE category (admin only)
# -----------------------
@router.put("/categories/{category_id}", response_model=CategorySchema)
def update_category(
    category_id: int,
    category: CategoryCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can update categories")

    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category

# -----------------------
# DELETE category (admin only)
# -----------------------
@router.delete("/categories/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can delete categories")

    db.delete(db_category)
    db.commit()
    return {"message": f"Category with ID {category_id} has been deleted"}
