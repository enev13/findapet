from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class AnimalBase(BaseModel):
    name: str
    description: str
