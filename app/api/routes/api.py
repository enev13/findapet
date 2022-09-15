from fastapi import APIRouter
from app.api.routes import animals, users

router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(animals.router, tags=["animals"], prefix="/animals")
