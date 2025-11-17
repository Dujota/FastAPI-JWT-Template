from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.review import ReviewModel
from serializers.review import ReviewSchema
from typing import List
from models.property import PropertyModel
from database import get_db

router = APIRouter()

#gets all reviews for a property
@router.get('/properties/{property_id}/reviews', response_model=List[ReviewSchema])
def get_properties(property_id: int, db: Session = Depends(get_db)):
  Property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first()
  if not property:
    raise HTTPException(status_code=404, detail="Property not found")

  return property.reviews

#gets a single review by id
@router.get('/properties/{reviews_id}', response_model=ReviewSchema)
def get_review(review_id: int, db: Session = Depends(get_db)):
  review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

  return review

#create a new review for given property id
@router.post('/properties/{property_id}/reviews', response_model=ReviewSchema)
def create_review(property_id: int, review: ReviewSchema, db: Session = Depends(get_db)):
    property = db.query(PropertyModel).filter(PropertyModel.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    new_review = ReviewModel(**review.dict(), property_id=property_id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review



@router.put("/reviews/{review_id}", response_model=ReviewSchema)
def update_review(review_id: int, review: ReviewSchema, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    review_data = review.dict(exclude_unset=True)
    for key, value in review_data.items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)
    return db_review

@router.delete("/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(db_review)
    db.commit()
    return {"message": f"Comment with ID {review_id} has been deleted"}