from typing import List, Optional

from app.models import enums
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class User(UserBase):
    id: int
    name: str
    last_name: Optional[str]
    location: Optional[str]
    role: enums.RoleType
    animals: Optional[List[int]]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"name": "Felix", "last_name": "Kanitz", "location": "Varna, Bulgaria", "role": "user"}
        }


class UserInCreate(UserBase):
    name: str
    last_name: Optional[str]
    location: Optional[str]
    password: str

    class Config:
        schema_extra = {"example": {"email": "felix@kanitz.com", "password": "koti"}}


class UserInLogin(UserBase):
    password: str
