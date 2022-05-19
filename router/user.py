from collections import UserString
import imp
from typing import List
from urllib import response
from  fastapi.responses import Response
from  fastapi  import  APIRouter, Depends,responses
from sqlalchemy.orm.session import Session
from  db import db_users
from db.database import get_db
from  schema import User, UserBase,UserDisplay




router = APIRouter(prefix='/users', tags=['users'])


# create User

@router.post('/add',
summary='add user',
response_model=UserDisplay
)
async def create_new(user: UserBase , db : Session= Depends(get_db)):
    """
    Permet ***d'ajouter un utilisateur***
    """
    return db_users.create_user(db,user)
    

# read Users

@router.get('/all',
summary='recuperer tous les utilisateur',
response_model= List[UserDisplay]
)
async def get_all(db : Session= Depends(get_db),response :Response=None ):
    """
    recuperation de tous les utilisateur
    
    """
    # all =db_users.get_all(db)
    # response = all
    # response.set_cookie(key='name', value='edouard')
    # return response
    return db_users.get_all(db)
    # data= " ".join(db_users.get_all(db))
    # return Response(content=data, media_type="text/pain")


# read one users
@router.get('/{id}',
summary='recuperer un utilisateur',
response_model= UserDisplay
)
async def get_one(id:int,db : Session= Depends(get_db)):
    """
    recuperation un utilisateur
    
    """
    return db_users.get_one(db,id)

    # data= " ".join(db_users.get_one(db,id))
    # return Response(content=db_users.get_one(db,id), media_type="text/pain")
# update Users

@router.put('/{id}',
summary='modifier  un utilisateur',

)
async def update_one(user: UserBase ,id:int,db : Session= Depends(get_db)):
    """
    modifier  un utilisateur
    
    """
    return db_users.update_user(db , id, user)


# delete Users

@router.delete('/{id}',
summary='supprimer  un utilisateur',

)
async def delete_one(id:int,db : Session= Depends(get_db)):
    """
    supprimer un utilisateur
    
    """
    return db_users.delete_user(db,id)