from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.database import get_db

router = APIRouter()


@router.get("/animals/", response_model=list[schemas.Animal])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_animals(db, skip=skip, limit=limit)
    return items
