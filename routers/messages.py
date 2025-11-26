from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import get_db

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/", response_model=schemas.MessageResponse)
def send_message(msg: schemas.MessageCreate, db: Session = Depends(get_db)):

    sender = db.query(models.User).filter(models.User.id == msg.sender_id).first()
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")

    room = db.query(models.Room).filter(models.Room.id == msg.room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return crud.create_message(db, msg)


@router.get("/{room_id}", response_model=list[schemas.MessageResponse])
def get_messages(room_id: int, db: Session = Depends(get_db)):

    room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return crud.get_messages_by_room(db, room_id)
