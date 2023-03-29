from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# from database import Base

from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine

# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     body = Column(String, index=True)
#     author_id = Column(Integer, ForeignKey('users.id'))
#     author = relationship("User", back_populates="posts")


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)
#     posts = relationship("Post", back_populates="author")
class UserBase(SQLModel):
    name: str
    email: str
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    posts: List["Post"] = Relationship(back_populates="author")

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

# Post
class PostBase(SQLModel):
    title: str
    body: str


class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="posts")

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int

# Auth
class Login(SQLModel):
    username: str
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    email: str | None = None
