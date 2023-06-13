# from fastapi import FastAPI, Path
# import pandas as pd
# import json as js
# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime
# from uuid import uuid4 as uuid

# dolar=pd.read_csv('DOLAR MEP - Cotizaciones historicas.csv')
# cols=['ultimo','fecha']
# dolar=dolar[cols]
# posts=[]

# # import uvicorn
# # Crear una instancia de la aplicación FastAPI
# app = FastAPI()

# #Post Model
# class Post(BaseModel):
#     id:Optional[str]
#     title:str
#     author:str
#     #content:Text 
#     create_at:datetime=datetime.now()
#     published_at:Optional[datetime]
#     published:bool=False
    


# # Definir una ruta y su función controladora
# @app.get("/")
# async def root():
#     return dolar.tail()
# # @app.get("/messi")
# # async def root():
# #     return '~!¡gato'
# @app.get('/posts')
# def get_posts():
#     return posts
# @app.post('/posts')
# def save_post(post:Post):
#     post.id=str(uuid())
#     posts.append(post.dict())
#     #return "receive"
#     return posts[-1]

# @app.get('/post/{post_id}')
# def get_post():
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import pandas as pd
import uvicorn

app = FastAPI()

class Dolar(BaseModel):
    id: Optional[str]
    # fecha:datetime
    # dolar:float
    fecha:datetime
    valor:float

@app.get('/dolar/{Fecha}')
async def get_posts(Fecha: str):

    dolard=pd.read_csv('DOLAR MEP - Cotizaciones historicas.csv')
    cols=['ultimo','fecha']

    dolard=dolard[cols].to_dict()
    for dolar in dolard:
        
        if dolar["fecha"].iloc[0] == str(Fecha):

            return dolar
    raise HTTPException(status_code=404, detail="Item not found")
    return posts

@app.get('/dolar')
async def get_posts():
    dolard=pd.read_csv('DOLAR MEP - Cotizaciones historicas.csv')
    cols=['ultimo','fecha']

    dolard=dolard[cols].tail().to_dict()
    return dolard;
# @app.post('/dolar')
# async def save_post():
#     dolard=pd.read_csv('DOLAR MEP - Cotizaciones historicas.csv')
#     cols=['ultimo','fecha']
#     dolard=dolard[cols].to_dict()
    
       
        
#     return dolard

# posts = []



