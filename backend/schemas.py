from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ActivityLogsBaseSchema(BaseModel):
    id: str
    title:str
    description:str


class ActivityLogsSchema(ActivityLogsBaseSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ActivityLogsCreateSchema(ActivityLogsBaseSchema):
    pass


class PostBaseSchema(BaseModel):
    title: str
    description: Optional[str] = None
    imageSrc: str
    created: datetime
    activity_logs: List[ActivityLogsSchema]


class PostSchema(PostBaseSchema):
    id: int
    owner_id: int


    class Config:
        orm_mode = True


class PostCreateSchema(PostBaseSchema):
    pass


class UserBaseSchema(BaseModel):
    username: str


class UserSchema(UserBaseSchema):
    id: int
    # posts: List[PostSchema] = []

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str


class TokenSchema(BaseModel):
    access_token: str