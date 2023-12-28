from typing import Optional, List
from sqlmodel import Field, SQLModel, Column, String, Relationship, UniqueConstraint
from pydantic import EmailStr
from datetime import datetime

class UsersBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(index=True)
    profile_pic: Optional[str] = None
    email: EmailStr = Field(index=True,unique=True )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class UsersRead(UsersBase):
    pass


 
class Users(UsersBase, table=True):
    __table_args__ = (
        UniqueConstraint( "id","email", name="your_unique_constraint_name"),
    )


    password: str = Field(sa_column=Column(String))
    # messages: List["Message"] = Relationship(back_populates="user")

 

class UserLogin(SQLModel):
    email: str
    password: str
class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    id: Optional[str] = None