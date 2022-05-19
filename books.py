from enum import Enum
from typing import Optional
from urllib import response
from  fastapi import FastAPI,status,Response
from  router import client
from  router  import  client_post

app =  FastAPI()


app.get("/",
tags="acceuil",
summary="page d'accueil",
description="page d'accueil  de  l'aplication"
)
async def get_all():
    return {"message": "all thing"}

app.include_router(client.router)
app.include_router(client_post.router)