from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    nombre: str = Field(..., min_length=1, max_length=50)
    apellido: str = Field(..., min_length=1, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    apellido: Optional[str] = Field(None, min_length=1, max_length=50)

class UserResponse(UserBase):
    id: int

    
class LoginRequest(BaseModel):
    username: str
    password: str