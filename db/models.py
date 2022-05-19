from turtle import back
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from db.database import Base

class DbUsers(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("DbArticles",  back_populates="user")


class DbArticles(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer , ForeignKey('users.id'))
    user = relationship("DbUsers", back_populates="items")
   