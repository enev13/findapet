"""Security module"""

from datetime import datetime, timedelta
from typing import Any, Union

from decouple import config
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from starlette.requests import Request

from app.models.enums import RoleType

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
ALGORITHM = "HS256"
JWT_SECRET_KEY = config("JWT_SECRET_KEY")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """Create a JWT token"""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def get_hashed_password(password: str) -> str:
    """Hash a password"""
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify a password"""
    return password_context.verify(password, hashed_pass)


def is_user(request: Request):
    """Check if the user is a 'user' role"""
    if not request.state.user["role"] == RoleType.user:
        raise HTTPException(403, "Forbidden")


def is_shelter(request: Request):
    """Check if the user is a 'shelter' role"""
    if not request.state.user["role"] == RoleType.shelter:
        raise HTTPException(403, "Forbidden")


def is_admin(request: Request):
    """Check if the user is a 'admin' role"""
    if not request.state.user["role"] == RoleType.admin:
        raise HTTPException(403, "Forbidden")


def is_current_user(request: Request, user_id: int):
    """Check if the user is the current user"""
    if not request.state.user["id"] == user_id:
        raise HTTPException(403, "Forbidden")
