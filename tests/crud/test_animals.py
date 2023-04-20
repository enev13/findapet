"""Tests CRUD operations for animals"""

from sqlalchemy.orm import Session

from app.db.crud.animals import create_animal, delete_animal, get_animal, get_animals, update_animal
from app.db.crud.users import create_user
from tests.utils.random import generate_random_animal_in, generate_random_user_in


def test_create_animal(db: Session) -> None:
    """Tests if animal is created"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    assert animal
    assert animal.name == animal_in.name


def test_get_animal(db: Session) -> None:
    """Tests if animal is retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    retrieved_animal = get_animal(db, animal_id=animal.id)

    assert retrieved_animal
    assert retrieved_animal.id == animal.id
    assert retrieved_animal.name == animal.name


def test_get_animals(db: Session) -> None:
    """Tests if animals are retrieved"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    create_animal(db, animal=animal_in)

    animals = get_animals(db)
    assert animals
    assert len(animals) > 0


def test_update_animal(db: Session) -> None:
    """Tests if animal is updated"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    new_animal_data = generate_random_animal_in()
    new_animal_data.owner_id = user.id
    updated_animal = update_animal(db, new_animal_data, animal.id)

    assert updated_animal
    assert updated_animal.id == animal.id
    assert updated_animal.name == new_animal_data.name


def test_delete_animal(db: Session) -> None:
    """Tests if animal is deleted"""
    user_in = generate_random_user_in()
    user = create_user(db, user=user_in)

    animal_in = generate_random_animal_in()
    animal_in.owner_id = user.id
    animal = create_animal(db, animal=animal_in)

    delete_animal(db, animal_id=animal.id)
    retrieved_animal = get_animal(db, animal_id=animal.id)
    assert not retrieved_animal
