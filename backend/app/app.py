from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

#local
from app.core.config import settings

#Local
from app.models.user_model import User


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    """
         initialize crucial application services
    """
    
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STIRING).todolist
    
    await init_beanie(
        database=db_client,
        document_models = [
            User
            
        ]
    )
    