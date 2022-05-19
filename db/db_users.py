
import email
from typing import List
from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from db.models import DbUsers
from  db.hash import Hash

from schema import UserBase


def  create_user(db: Session,  request: UserBase):
    new_user= DbUsers(
        first_name =request.first_name,
        email= request.email,
        hashed_password= Hash.bcrypt(request.password),
        # is_active= request.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def  get_all(db: Session):
    all: List[DbUsers]
    if  not all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user   not found')
    all= db.query(DbUsers).all()
    
    return all

def  get_one(db: Session, id: int):
    return db.query(DbUsers).filter(DbUsers.id == id ).first()

    
def  get_user_by_username(db: Session, id: str):
    return db.query(DbUsers).filter(DbUsers.first_name == id ).first()

     
def  update_user(db: Session,  id:int,request: UserBase):
    user = db.query(DbUsers).filter(DbUsers.id == id)
    if  not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    user.update ({
            DbUsers.first_name :request.first_name,
            DbUsers.email:request.email,
            DbUsers.hashed_password: Hash.bcrypt(request.password)
            # is_active= request.is_active
    })
    
    db.commit()
       
    return 'ok'

def  delete_user(db: Session,  id:int):
    user = db.query(DbUsers).filter(DbUsers.id == id).first()
    if  not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    db.delete(user)
    db.commit()
       
    return 'ok'