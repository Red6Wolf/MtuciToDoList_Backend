from typing import Optional
from pydantic import BaseModel,EmailStr, Field, validator
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length = 4, max_length = 20, description="user username (between 4 and 20 characters)")
    password: str = Field(..., min_length = 6, max_length = 30,description="user password (between 6 and 30 characters)")
    
class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False
    