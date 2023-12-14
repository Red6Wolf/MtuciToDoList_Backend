from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    
    #Обновление токена и его срок истечения в 7 дней
    
    ACEESS_TOKEN_EPIRE_MINUTES: int = 15               
    REFRESH_TOKEN_EMPIRE_MINUTES: int = 60  * 24 * 7 
    BACEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "TODOLIST"
    
    #DataBase
    MONGO_CONNECTION_STIRING: str = config("MONGO_CONNECTION_STRING", cast = str)
    class Config: 
        case_sensitive = True
        
settings = Settings()
project_name = settings.PROJECT_NAME