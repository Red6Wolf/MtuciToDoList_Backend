from typing import Union, Any
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

#local
from app.core.config import settings


password_context = CryptContext(schemes=['bcrypt'], deprecated = "auto" )

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes = settings.ACEESS_TOKEN_EPIRE_MINUTES)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
        return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes = settings.REFRESH_TOKEN_EMPIRE_MINUTES)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        
        encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
        return encoded_jwt