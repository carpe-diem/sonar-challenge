from typing import OrderedDict

from sqlalchemy.orm import Session

from models import User, Post
from schemas import UserSchema


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(User).offset(skip).limit(limit).all()


def get_all_posts(db: Session, skip: int=0, limit: int=10):
    items = db.query(Post).order_by(-Post.id).offset(skip).limit(limit).all()
    posts = []
    for item in items:
        post = OrderedDict()
        post["id"] = item.id
        post["title"] =  item.title
        post["imageSrc"] = item.imageSrc
        posts.append(post)
    return posts

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


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