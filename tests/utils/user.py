from sqlalchemy.orm import Session

from app.db import crud
from app.models.users import User
from app.schemas.users import UserInCreate
from tests.utils.utils import random_email, random_lower_string


def create_random_user(db: Session) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserInCreate(email=email, password=password)
    user = crud.create_user(db=db, user=user_in)
    return user
