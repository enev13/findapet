from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

# from app.core.security import verify_password
from app.db import crud
from app.schemas.users import UserInCreate  # , UserUpdate
from tests.utils.utils import random_email, random_lower_string


def test_create_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    name = random_lower_string()
    last_name = random_lower_string()
    user_in = UserInCreate(email=email, password=password, name=name, last_name=last_name)
    user = crud.create_user(db, user=user_in)
    assert user.email == email
    assert hasattr(user, "password")


def test_get_user(db: Session) -> None:
    password = random_lower_string()
    username = random_email()
    name = random_lower_string()
    last_name = random_lower_string()
    user_in = UserInCreate(email=username, password=password, name=name, last_name=last_name)
    user = crud.create_user(db, user=user_in)
    user_2 = crud.get_user(db, user_id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


# def test_update_user(db: Session) -> None:
#     password = random_lower_string()
#     email = random_email()
#     name = random_lower_string()
#     last_name = random_lower_string()
#     user_in = UserInCreate(email=email, password=password, name=name, last_name=last_name)
#     user = crud.users.create_user(db, obj_in=user_in)
#     new_password = random_lower_string()
#     user_in_update = UserUpdate(password=new_password, name=name, last_name=last_name)
#     crud.user.update(db, db_obj=user, obj_in=user_in_update)
#     user_2 = crud.user.get(db, id=user.id)
#     assert user_2
#     assert user.email == user_2.email
#     assert verify_password(new_password, user_2.hashed_password)
