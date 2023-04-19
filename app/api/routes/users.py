"""This module contains the routes for the users endpoint."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.database import get_db

# from app.core.security import oauth2_scheme

router = APIRouter()


@router.get("/users/", response_model=List[schemas.User])
def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)  # , token: str = Depends(oauth2_scheme)
):
    """Get all users"""
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Get a single user"""
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}/animals", response_model=List[schemas.Animal])
def read_user_animals(user_id: int, db: Session = Depends(get_db)):
    """Get all animals for a user"""
    return crud.get_animals_by_user(db=db, user_id=user_id)


@router.patch("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserInUpdate, db: Session = Depends(get_db)):
    """Update a user"""
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user=user)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)
