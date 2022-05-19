from ast import Import
from email.mime import application
from multiprocessing.spawn import import_main_path
from operator import mod
from  fastapi import FastAPI
from router  import client
from  router  import  client_post
from  db  import models
from auth  import  authentication
from router  import article
from  db.database  import  engine  
from  router import user,file
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/',
summary='accueil  de  l api'
)
async  def  get_all():
    return {'message': 'accueil de  l application'}
app.include_router(authentication.router)
app.include_router(article.router)
app.include_router(client.router)
app.include_router(client_post.router)
app.include_router(file.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)
app.mount('/files', StaticFiles(directory="files"), name='files')