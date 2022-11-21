from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ActivityLogsBase(BaseModel):
    id: str
    title:str
    description:str


class ActivityLogs(ActivityLogsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ActivityLogsCreate(ActivityLogsBase):
    pass


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None
    imageSrc: str
    created: datetime
    activity_logs: List[ActivityLogs]


class Post(PostBase):
    id: int
    owner_id: int


    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class Token(BaseModel):
    access_token: str