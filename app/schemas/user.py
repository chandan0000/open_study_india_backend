from typing import Optional, List
from sqlmodel import Field, SQLModel, Column, String, Relationship
from pydantic import EmailStr
from datetime import datetime

class UsersBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(index=True)
    profile_pic: Optional[str] = None
    email: EmailStr = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class UsersRead(UsersBase):
    id: int

class UsersCreate(UsersBase, table=True):
    password: str = Field(sa_column=Column(String))
 
# class Users(UsersBase, table=True):
#     password: str = Field(sa_column=Column(String))
#     messages: List["Message"] = Relationship(back_populates="user")

 

class UserLogin(SQLModel):
    email: str
    password: str
