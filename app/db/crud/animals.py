"""CRUD operations for animals."""

from typing import List

from sqlalchemy.orm import Session

from app import models, schemas


def get_animals(db: Session, skip: int = 0, limit: int = 1000) -> List[schemas.Animal]:
    """Get all animals."""
    return db.query(models.Animal).offset(skip).limit(limit).all()


def get_animals_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[schemas.Animal]:
    """Get all animals by user."""
    return db.query(models.Animal).filter(models.Animal.owner_id == user_id).offset(skip).limit(limit).all()


def get_animal(db: Session, animal_id: int) -> schemas.Animal:
    """Get an animal by id."""
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()


def create_animal(db: Session, animal: schemas.AnimalInCreateUpdate) -> schemas.Animal:
    """Create a new animal."""
    db_animal = models.Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


def update_animal(db: Session, animal: schemas.AnimalInCreateUpdate, animal_id: int) -> schemas.Animal:
    """Update an animal."""
    db_animal = db.query(models.Animal).filter(models.Animal.id == animal_id).first()
    for key, value in animal.dict(exclude_unset=True).items():
        setattr(db_animal, key, value)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


def delete_animal(db: Session, animal_id: int):
    """Delete an animal."""
    db.query(models.Animal).filter(models.Animal.id == animal_id).delete()
    db.commit()
