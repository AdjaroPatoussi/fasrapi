

from tkinter import E
from typing import List
from pydantic import BaseModel


class Article(BaseModel):
    title : str
    content: str
    class Config():
        orm_mode= True

class User(BaseModel):
    email: str
    first_name: str
    is_active: bool
    class Config():
        orm_mode= True


        

class  UserBase(BaseModel):
   
    email: str
    first_name: str
    password: str
    # is_active: bool
class  UserDisplay(BaseModel):
   
    email: str
    first_name: str
    is_active: bool
    items: List[Article] = []
    class Config():
        orm_mode= True



class ArticleDisplay(BaseModel):
    title : str
    content: str
    user=User
    class Config():
        orm_mode= True
class ArticleBase(BaseModel):
    title : str
    content: str
    user_id : int

