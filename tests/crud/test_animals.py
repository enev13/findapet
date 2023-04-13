"""Tests CRUD operations for animals"""

from sqlalchemy.orm import Session

from app.db import crud

from app.schemas.animals import Animal
from tests.utils.random import generate_random_animal_data


def generate_random_animal_in() -> Animal:
    """Generates random animal data for Animal schema"""
    animal_in = generate_random_animal_data()
    return Animal(**animal_in)


def test_create_animal(db: Session) -> None:
    """Tests if animal is created"""
    animal_in = generate_random_animal_in()
    animal = crud.create_animal(db, animal=animal_in)
    assert animal
    assert animal.name == animal_in.name


def test_get_animal(db: Session) -> None:
    """Tests if animal is retrieved"""
    animal_in = generate_random_animal_in()
    animal = crud.create_animal(db, animal=animal_in)
    retrieved_animal = crud.get_animal(db, animal_id=animal.id)
    assert retrieved_animal
    assert retrieved_animal.id == animal.id
    assert retrieved_animal.name == animal.name


def test_get_animals(db: Session) -> None:
    """Tests if animals are retrieved"""
    animal_in = generate_random_animal_in()
    animal = crud.create_animal(db, animal=animal_in)
    animals = crud.get_animals(db)
    assert animals
    assert animals[0].id == animal.id
    assert animals[0].name == animal.name


def test_update_animal(db: Session) -> None:
    """Tests if animal is updated"""
    animal_in = generate_random_animal_in()
    animal = crud.create_animal(db, animal=animal_in)
    new_animal_data = generate_random_animal_in()
    updated_animal = crud.update_animal(db, new_animal_data, animal.id)
    assert updated_animal
    assert updated_animal.id == animal.id
    assert updated_animal.name == new_animal_data.name


def test_delete_animal(db: Session) -> None:
    """Tests if animal is deleted"""
    animal_in = generate_random_animal_in()
    animal = crud.create_animal(db, animal=animal_in)
    crud.delete_animal(db, animal_id=animal.id)
    retrieved_animal = crud.get_animal(db, animal_id=animal.id)
    assert not retrieved_animal
