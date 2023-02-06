from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.database import get_db
from app.core.security import oauth2_scheme

router = APIRouter()


@router.get("/users/", response_model=list[schemas.User])
def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)  # , token: str = Depends(oauth2_scheme)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
