from collections import UserString
from typing import List
from  fastapi  import  APIRouter, Depends
from sqlalchemy.orm.session import Session
from  db import db_article
from  db import db_users
from db.database import get_db
from  schema import ArticleBase,ArticleDisplay
from  auth.oauth2 import oauth2_bearer


router = APIRouter(prefix='/article', tags=['article'])


# create Article

@router.post('/add',
summary='add article',
response_model=ArticleDisplay
)
async def create_new(article: ArticleBase , db : Session= Depends(get_db),auth: str =Depends(oauth2_bearer)):
    """
    Permet ***d'ajouter un article***
    """
    return db_article.create_Article(db,article)
    

# read Article

@router.get('/all',
summary='recuperer tous les articles',
response_model= List[ArticleDisplay]
)
async def get_all(db : Session= Depends(get_db)):
    """
    recuperation de tous les articles
    
    """
    return db_article.get_all(db)


# read one Article
@router.get('/{id}',
summary='recuperer un utilisateur',
response_model= ArticleDisplay
)
async def get_one(id:int,db : Session= Depends(get_db)):
    """
    recuperation tous les articles
    
    """
    return db_article.get_one(db,id)


# update Artice

@router.put('/{id}',
summary='modifier  un article',

)
async def update_one(article:ArticleBase ,id:int,db : Session= Depends(get_db)):
    """
    modifier  un article
    
    """
    return db_article.update_article(db , id, article)


# delete Article

@router.delete('/{id}',
summary='supprimer  un article',

)
async def delete_one(id:int,db : Session= Depends(get_db)):
    """
    supprimer un article
    
    """
    return db_article.delete_article(db,id)