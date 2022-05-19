from enum import Enum
from typing import Optional
from fastapi  import  APIRouter,Response,status

router = APIRouter (prefix='/client', tags=['client'])


class  TypeCLient(str, Enum):
    particulier= "particulier",
    grossiste= "grossite"

@router.get('/',
summary="tous les client",
description="avoir tous les clients"
    )
async def get_all():
    return {"message":"mesaage"}


@router.get('/{id}',
status_code= status.HTTP_404_NOT_FOUND,
summary= "get one client"
)
async  def get_one(id:TypeCLient, response: Response= None, page = 10, page_size: Optional[int]=None):
    """
    recuperer  un  client 

    - **id** represente l'id du  client
    - **page** represente le nombre de page

    
    """
    if(id == 0 ):
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"error": "id can't be  null"}

    if(id<0):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return{"error": "id can  not be negative"}
    
    response.status_code= status.HTTP_200_OK
    return   {"message": f"client  numero  {id}, \n page {page}, taille de la page {page_size}"}