from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.database import get_db

router = APIRouter()


@router.get("/animals/", response_model=list[schemas.Animal])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_animals(db, skip=skip, limit=limit)
    return items


@router.get("/animals/{animal_id}", response_model=schemas.Animal)
def read_animal(animal_id: int, db: Session = Depends(get_db)):
    db_animal = crud.get_animal(db, animal_id=animal_id)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return db_animal


@router.post("/animals/", response_model=schemas.Animal)
def create_animal_for_user(user_id: int, item: schemas.Animal, db: Session = Depends(get_db)):
    return crud.create_animal(db=db, item=item, user_id=user_id)
