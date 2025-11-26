# routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    try:
        new_user = crud.create_user(db, user)
        return new_user
    except IntegrityError:
        # duplicate race condition or DB level unique constraint
        raise HTTPException(status_code=400, detail="Username already exists")
    except Exception as e:
        # log server-side for debugging
        print("Router create_user error:", repr(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
