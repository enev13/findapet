from typing import List, Optional

from app.models import enums
from app.schemas.base import UserBase


class User(UserBase):
    id: int
    name: Optional[str]
    last_name: Optional[str]
    location: Optional[str]
    role: Optional[enums.RoleType] = enums.RoleType.user
    animals: Optional[List[int]]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"name": "Felix", "last_name": "Kanitz", "location": "Varna, Bulgaria", "role": "user"}
        }


class UserInCreate(UserBase):
    name: Optional[str]
    last_name: Optional[str]
    location: Optional[str]
    password: str

    class Config:
        schema_extra = {"example": {"email": "felix@kanitz.com", "password": "koti"}}


class UserInLogin(UserBase):
    password: str

    class Config:
        orm_mode = True
