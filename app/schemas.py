from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    #Forbid extra/NEW key in input JSON while PATCH-ing
    class Config:
        extra = "forbid"

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr