from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas
from app.core.security import create_access_token, verify_password
from app.db import crud
from app.db.database import get_db

router = APIRouter()


@router.post("/register/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserInCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email is already registered")
    return crud.create_user(db=db, user=user)


@router.post("/login/", response_model=schemas.Token)
def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=form_data.username)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")

    hashed_pass = db_user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    return {"access_token": create_access_token(form_data.username), "token_type": "Bearer"}
