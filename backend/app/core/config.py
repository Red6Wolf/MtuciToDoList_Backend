from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)