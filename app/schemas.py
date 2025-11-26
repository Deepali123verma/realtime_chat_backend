from pydantic import BaseModel
from datetime import datetime


# -----------------------------------
# USER
# -----------------------------------
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True   # Pydantic v2 replacement for orm_mode
    }


# -----------------------------------
# ROOM
# -----------------------------------
class RoomBase(BaseModel):
    name: str


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


# -----------------------------------
# MESSAGE
# -----------------------------------
class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    sender_id: int
    room_id: int


class MessageResponse(MessageBase):
    id: int
    sender_id: int
    room_id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }


# -----------------------------------
# AUTHENTICATION SCHEMAS
# -----------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# Used in /auth/login (JSON body login)
class UserLogin(BaseModel):
    username: str
    password: str
