"""Test CRUD operations for user."""

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.db.crud.animals import create_animal, get_animals_by_user
from app.db.crud.users import (
    authenticate_user,
    create_user,
    delete_user,
    get_user,
    get_user_by_email,
    get_users,
    update_user,
)
from app.schemas.users import UserInUpdate
from tests.utils.random import generate_random_animal_in, generate_random_user_in
from tests.utils.utils import random_lower_string


def test_create_user(db: Session) -> None:
    """Tests if user is created"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    assert user.email == user_in.email
    assert hasattr(user, "password")


def test_get_user(db: Session) -> None:
    """Tests if user is retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    user_2 = get_user(db, user_id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_user_by_email(db: Session) -> None:
    """Tests if user is retrieved by email"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    user_2 = get_user_by_email(db, email=user_in.email)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_users(db: Session) -> None:
    """Tests if users are retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    users = get_users(db, skip=0, limit=100)
    assert users
    for u in users:
        if u.email == user.email:
            assert jsonable_encoder(u) == jsonable_encoder(user)
            break


def test_update_user(db: Session) -> None:
    """Tests if user is updated"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    user.location = random_lower_string()
    user_update = UserInUpdate(**user.__dict__)
    user2 = update_user(db, user_id=user.id, user=user_update)
    assert user2
    assert user.id == user2.id
    assert user.location == user2.location


def test_delete_user(db: Session) -> None:
    """Tests if user is deleted"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    delete_user(db, user_id=user.id)
    user2 = get_user(db, user_id=user.id)
    assert user2 is None


def test_change_password(db: Session) -> None:
    """Tests if password is changed"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)
    new_password = random_lower_string()
    user.password = new_password
    user_update = UserInUpdate(**user.__dict__)
    user2 = update_user(db, user_id=user.id, user=user_update)
    assert user2
    assert user.id == user2.id
    assert verify_password(new_password, user2.password)


def test_authenticate_user(db: Session) -> None:
    """Tests if user is authenticated"""
    user_in = generate_random_user_in()
    email = user_in.email
    password = user_in.password
    user = create_user(db, user=user_in)
    authenticated_user = authenticate_user(db, email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email
    assert jsonable_encoder(user) == jsonable_encoder(authenticated_user)


def test_get_all_animals_for_user(db: Session) -> None:
    """Tests if user's animals are retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    create_animal(db, animal=animal_in)

    animals = get_animals_by_user(db, user_id=user.id)
    assert animals
    for a in animals:
        assert a.owner_id == user.id
