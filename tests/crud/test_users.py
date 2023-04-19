"""Test CRUD operations for user."""

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.db import crud
from app.schemas.users import UserInCreate, UserInUpdate
from tests.utils.random import generate_random_user_data
from tests.utils.utils import random_lower_string


def generate_random_user_in() -> UserInCreate:
    """Generates a random user"""
    user_in = generate_random_user_data()
    return UserInCreate(**user_in)


def test_create_user(db: Session) -> None:
    """Tests if user is created"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    assert user.email == user_in.email
    assert hasattr(user, "password")


def test_get_user(db: Session) -> None:
    """Tests if user is retrieved"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    user_2 = crud.get_user(db, user_id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_user_by_email(db: Session) -> None:
    """Tests if user is retrieved by email"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    user_2 = crud.get_user_by_email(db, email=user_in.email)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_users(db: Session) -> None:
    """Tests if users are retrieved"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    users = crud.get_users(db, skip=0, limit=100)
    assert users
    for u in users:
        if u.email == user.email:
            assert jsonable_encoder(u) == jsonable_encoder(user)
            break


def test_update_user(db: Session) -> None:
    """Tests if user is updated"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    user.location = random_lower_string()
    user_update = UserInUpdate(**user.__dict__)
    user2 = crud.update_user(db, user_id=user.id, user=user_update)
    assert user2
    assert user.id == user2.id
    assert user.location == user2.location


def test_delete_user(db: Session) -> None:
    """Tests if user is deleted"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    crud.delete_user(db, user_id=user.id)
    user2 = crud.get_user(db, user_id=user.id)
    assert user2 is None


def test_change_password(db: Session) -> None:
    """Tests if password is changed"""
    user_in = generate_random_user_in()
    user = crud.create_user(db, user=user_in)
    new_password = random_lower_string()
    user.password = new_password
    user_update = UserInUpdate(**user.__dict__)
    user2 = crud.update_user(db, user_id=user.id, user=user_update)
    assert user2
    assert user.id == user2.id
    assert verify_password(new_password, user2.password)


def test_authenticate_user(db: Session) -> None:
    """Tests if user is authenticated"""
    user_in = generate_random_user_in()
    email = user_in.email
    password = user_in.password
    print("user_in.password:", user_in.password)
    user = crud.create_user(db, user=user_in)
    authenticated_user = crud.authenticate_user(db, email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email
    assert jsonable_encoder(user) == jsonable_encoder(authenticated_user)
