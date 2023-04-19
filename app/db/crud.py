""" CRUD operations for the database. """

from typing import List
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import ALGORITHM, JWT_SECRET_KEY, get_hashed_password, oauth2_scheme, verify_password
from app.db import crud


def get_user(db: Session, user_id: int):
    """Get a user by id."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users."""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInCreate) -> schemas.User:
    """Create a new user."""
    user.password = get_hashed_password(user.password)
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserInUpdate) -> schemas.User:
    """Update a user."""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if user.password:
        user.password = get_hashed_password(user.password)
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    """Delete a user."""
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()


def authenticate_user(db: Session, email: str, password: str) -> schemas.User:
    """Authenticate a user."""
    user = crud.get_user_by_email(db, email=email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(db: Session, token: str = Depends(oauth2_scheme)) -> schemas.User:
    """Get the current user."""
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.UserBase(email=email)
    except JWTError as ex:
        raise credentials_exception from ex
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


def get_animals(db: Session, skip: int = 0, limit: int = 1000) -> List[schemas.Animal]:
    """Get all animals."""
    return db.query(models.Animal).offset(skip).limit(limit).all()


def get_animals_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[schemas.Animal]:
    """Get all animals by user."""
    return db.query(models.Animal).filter(models.Animal.user_id == user_id).offset(skip).limit(limit).all()


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
