from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlmodel import Session
from ..models import  user_model
from ..schemas.user import Users

from .. import utils, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=user_model.UsersRead)
async def create_user(userModel: user_model.UsersModel, db: Session = Depends(get_db)):
    user=Users(**userModel.model_dump())
    # Check if email already exists
    existing_user = db.query(Users).filter(Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# list of user
@router.get('/list', response_model=List[user_model.UsersRead])
async def get_user( db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user) ):
    # user = db.query(Users).all()
    user = db.query(Users).filter(Users.id == current_user.id).all()

    return user

@router.get('/{id}', response_model=user_model.UsersRead)
async def get_user(id: int, db: Session = Depends(get_db),):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user

# db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user) 