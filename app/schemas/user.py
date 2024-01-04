from typing import Optional, List
from sqlmodel import Field, SQLModel, Column, String, UniqueConstraint
from pydantic import BaseModel
import pydantic as pd
from datetime import datetime

class UsersBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(index=True)
    profile_pic: Optional[str] = None
    email: str = Field(index=True,unique=True )

class UsersRead(UsersBase):
    id:int




 
class Users(UsersBase, table=True):
    __table_args__ = (
        UniqueConstraint( "id","email", name="your_unique_constraint_name"),
    )

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    password: str = Field(sa_column=Column(String))
    # messages: List["Message"] = Relationship(back_populates="user")

 





class TokenData(SQLModel):
    id: int | None = None  
class Token(BaseModel):
    access_token: str
    token_type: str