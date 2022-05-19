from typing import Optional
from pydantic import BaseModel


class  ClientModel(BaseModel):
    nom:str
    prenom:str
    age:Optional[int]