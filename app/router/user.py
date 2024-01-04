from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlmodel import Session, select
from ..models import  user_model
from ..schemas.user import Users ,UsersRead

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
    existing_user = db.query(Users).all()
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
# @router.get('/list', response_model=List[UsersRead])
# async def get_user( db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user) ):
#     # user = db.query(Users).all()
#     user = db.query(Users).filter(Users.id == current_user.id).all()

#     return user
# @router.get('/list', )
# async def get_users(db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
#     users = db.query(select(Users)).all()
#     return users

@router.get('/list', response_model=List[user_model.UsersRead])
async def get_user(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # users_subquery = select(Users).subquery()  # Use subquery method here

    # Now, use the subquery in the main query
    users = db.exec(select(Users)).all()

    return users

@router.get('/{id}', response_model=user_model.UsersRead)
async def get_user(id: int, db: Session = Depends(get_db),):
    user = db.query(Users).filter(Users.id == id).get()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user

# db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user) 