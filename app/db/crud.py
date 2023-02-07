from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import get_hashed_password


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInCreate) -> schemas.User:
    user.password = get_hashed_password(user.password)
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserInUpdate) -> schemas.User:
    if isinstance(user, dict):
        update_data = user
    else:
        update_data = user.dict(exclude_unset=True)
    if update_data["password"]:
        password = get_hashed_password(update_data["password"])
        del update_data["password"]
        update_data["password"] = password
    db_user = models.User(**update_data)
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_animals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Animal).offset(skip).limit(limit).all()


def get_animal(db: Session, animal_id: int):
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()


def create_animal(db: Session, animal: schemas.Animal, user_id: int):
    db_animal = models.Animal(**animal.dict(), owner_id=user_id)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal
