# app/crud.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
from app.auth import get_password_hash

# ==========================
# USER CRUD
# ==========================
def create_user(db: Session, user: schemas.UserCreate):
    try:
        hashed_password = get_password_hash(user.password)
        new_user = models.User(
            username=user.username,
            password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as e:
        db.rollback()
        # Let caller handle this (router -> HTTPException)
        raise
    except Exception as e:
        db.rollback()
        print("ERROR in create_user:", repr(e))
        raise

def get_user_by_username(db: Session, username: str):
    try:
        return db.query(models.User).filter(models.User.username == username).first()
    except Exception as e:
        print("ERROR in get_user_by_username:", repr(e))
        raise

# ==========================
# ROOM CRUD
# ==========================
def create_room(db: Session, room: schemas.RoomCreate):
    new_room = models.Room(name=room.name)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

def get_all_rooms(db: Session):
    return db.query(models.Room).all()

# ==========================
# MESSAGE CRUD
# ==========================
def create_message(db: Session, msg: schemas.MessageCreate):
    # optional: validate existence
    user = db.query(models.User).filter(models.User.id == msg.sender_id).first()
    room = db.query(models.Room).filter(models.Room.id == msg.room_id).first()
    if not user:
        raise ValueError(f"User with id {msg.sender_id} not found")
    if not room:
        raise ValueError(f"Room with id {msg.room_id} not found")

    new_msg = models.Message(
        content=msg.content,
        sender_id=msg.sender_id,
        room_id=msg.room_id
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

def get_messages_by_room(db: Session, room_id: int):
    return db.query(models.Message).filter(models.Message.room_id == room_id).all()
