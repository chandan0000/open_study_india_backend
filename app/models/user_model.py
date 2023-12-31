from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UsersBase(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(index=True)
    profile_pic: Optional[str] = None
    email: EmailStr = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class UsersRead(UsersBase):
    id: int
    # class Config:
    #     orm_mode = True

class UsersModel(UsersBase,):
    password: str 



class TokenData(BaseModel):
    id: Optional[str] = None
class Token(BaseModel):
    access_token: str
    token_type: str
