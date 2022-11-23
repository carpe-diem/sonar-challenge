import datetime
import enum

from sqlalchemy import DateTime, Column, Enum, ForeignKey, Integer, String,select,func, and_
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, column_property

from database import Base


class InteractionType(enum.Enum):
    Like = 1
    View = 2


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    salt= Column(String)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    imageSrc = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
    activity_logs = relationship("ActivityLogs", back_populates="post") 

    @hybrid_property
    def likes(self):
        return len([x for x in self.activity_logs if x.interaction_type == InteractionType.Like])


class ActivityLogs(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    interaction_type = Column(Enum(InteractionType))

    user = relationship("User")
    post = relationship("Post", back_populates="activity_logs")

