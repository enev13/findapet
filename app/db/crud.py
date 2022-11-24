from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import get_hashed_password


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserInCreate):
    user.password = get_hashed_password(user.password)
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_animals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Animal).offset(skip).limit(limit).all()


def create_user_animal(db: Session, animal: schemas.Animal, user_id: int):
    db_animal = models.Animal(**animal.dict(), owner_id=user_id)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal
