from fastapi import APIRouter

#local
from app.api.api_v1.handlers import user

router = APIRouter()
router.include_router(user.user_router, prefix='/user', tags=["users"])
