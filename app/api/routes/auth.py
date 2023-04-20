"""This module contains the authentication routes for the API."""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas
from app.api.routes.users import router as user_router
from app.core.security import create_access_token
from app.db.crud.users import authenticate_user, create_user, get_user_by_email
from app.db.database import get_db

router = APIRouter()


@user_router.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
@router.post("/register/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserInCreate, db: Session = Depends(get_db)) -> schemas.User:
    """Create a new user"""
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email is already registered")
    return create_user(db=db, user=user)


@router.post("/login/", response_model=schemas.Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> schemas.Token:
    """Authenticate a user"""
    authenticate_user(db, email=form_data.username, password=form_data.password)
    return {"access_token": create_access_token(form_data.username), "token_type": "Bearer"}


# @router.get("/users/me/", response_model=schemas.User)
# def read_users_me(current_user: schemas.User = Depends(crud.get_current_user)):
#     """Get the current user"""
#     return current_user
