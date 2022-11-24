from pydantic import BaseModel, EmailStr


class AnimalBase(BaseModel):
    name: str
    description: str


class UserBase(BaseModel):
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
