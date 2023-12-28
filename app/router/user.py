from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas import user
from .. import utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED,)
async def create_user(user: user.UsersCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# @router.get('/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db), ):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id: {id} does not exist")

#     return user