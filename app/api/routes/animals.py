"""This module contains the routes for the animals endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.db.crud.animals import get_animal, get_animals
from app.db.database import get_db

router = APIRouter()


@router.get("/animals/", response_model=List[schemas.Animal])
def read_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all animals"""
    items = get_animals(db, skip=skip, limit=limit)
    return items


@router.get("/animals/{animal_id}", response_model=schemas.Animal)
def read_animal(animal_id: int, db: Session = Depends(get_db)):
    """Get a single animal"""
    db_animal = get_animal(db, animal_id=animal_id)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return db_animal


@router.post("/animals/", response_model=schemas.Animal, status_code=status.HTTP_201_CREATED)
def create_animal(animal: schemas.AnimalInCreateUpdate, db: Session = Depends(get_db)):
    """Create a new animal"""
    return create_animal(db=db, animal=animal)


@router.patch("/animals/{animal_id}", response_model=schemas.Animal)
def update_animal(animal_id: int, animal: schemas.AnimalInCreateUpdate, db: Session = Depends(get_db)):
    """Update an animal"""
    db_animal = get_animal(db=db, animal_id=animal_id)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return update_animal(db=db, animal_id=animal_id, animal=animal)


@router.delete("/animals/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Delete an animal"""
    return delete_animal(db=db, animal_id=animal_id)
