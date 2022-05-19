

from typing import List
from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from db.models import DbArticles
from  db.hash import Hash

from schema import ArticleBase


def  create_Article(db: Session,  request: ArticleBase):
    new_article= DbArticles(
        title = request.title,
        content = request.content,
        user_id = request.user_id
        # is_active= request.is_active
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def  get_all(db: Session):
    all: List[DbArticles]
    if  not all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'article not found')
    all= db.query(DbArticles).all()
    return all

def  get_one(db: Session, id: int):
    return db.query(DbArticles).filter(DbArticles.id == id ).first()


def  update_article(db: Session,  id:int,request: ArticleBase):
    article = db.query(DbArticles).filter(DbArticles.id == id)
    if  not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    article.update ({
            DbArticles.content :request.first_name,
            DbArticles.title:request.email,
            DbArticles.user_id: request.user_id,

            # is_active= request.is_active
    })
        
    db.commit()
       
    return 'ok'

def  delete_article(db: Session,  id:int):
    article = db.query(DbArticles).filter(DbArticles.id == id).first()
    if  not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    db.delete(article)
    db.commit()
    return 'ok'