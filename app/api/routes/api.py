from fastapi import APIRouter

from app.api.routes import animals, auth, users

router = APIRouter()
router.include_router(animals.router, tags=["animals"])
router.include_router(auth.router, tags=["auth"])
router.include_router(users.router, tags=["users"])
