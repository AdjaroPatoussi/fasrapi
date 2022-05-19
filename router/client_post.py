from http.client import ImproperConnectionState
from typing import List, Optional
from  fastapi  import  APIRouter,Body,Query
from pydantic import BaseModel
# //from  Client_model import  ClientModel

router =  APIRouter(prefix='/client', tags=['client'])



class  ClientModel(BaseModel):
    nom:str
    prenom:str
    age:Optional[int]

@router.post('/new/{id}')
async def insert_client(client:ClientModel,id:int,email:str = Body(...,
                                                                min_length= 4,
                                                                max_length=8,
                                                                regex='^[a-z]*$'
                                                                
                                                                ),
                                                                list :Optional[List[str]] = Query(None)
                                                                ):
    
    
    return{
        "id":  id,
        'data': client,
        'email':email,
        'list':list
        }