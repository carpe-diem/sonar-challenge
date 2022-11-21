import base64
import hashlib
import os
from typing import OrderedDict

from sqlalchemy.orm import Session

from models import User, Post
from schemas import UserSchema, UserCreateSchema, PostCreateSchema


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreateSchema):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
                            'sha256',
                            user.password.encode('utf-8'),
                            salt,
                            100000) # It is recommended to use at least 100000 iterations of SHA-256    

    encodedSalt = base64.b64encode(salt)
    encodedKey = base64.b64encode(key)
     
    db_user = User(username=user.username, password=encodedKey.decode('utf-8'), salt=encodedSalt.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_post(db: Session, post: PostCreateSchema, user_id: int):
    db_post = Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db.refresh(db_post)


def get_user_posts(db: Session, user: UserSchema, skip: int=0, limit: int=10):
    items = db.query(Post).filter_by(owner_id=user.id).offset(skip).limit(limit).all()
    posts = []

    for item in items:
        post = OrderedDict()
        post["id"] = item.id
        post["title"] =  item.title
        post["description"] = item.description
        post["created"] = item.created
        post["imageSrc"] = item.imageSrc
        post["owner"] = item.owner.username
        posts.append(post)

    return posts