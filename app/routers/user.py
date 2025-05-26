from ..database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, HTTPException, status, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix= "/users",
    tags = ['Users']
)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user : schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        hashsed_password = utils.hash(user.password)
        user.password = hashsed_password
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except IntegrityError as e:
        db.rollback()
        if 'unique constraint' in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred."
            )
    
@router.get("/{id}", response_model=schemas.UserOut)
def get_users(id : int,db : Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return  user
    