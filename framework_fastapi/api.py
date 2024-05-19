# Importando fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn


# guardando la api en una variable
app = FastAPI()


# Creando una ruta o endpoint
@app.get("/")
def home():
    return {"Mensaje": "Hola mundo"}


# Creando una lista para simular una base de datos
publicaciones = []


# Creando una clase para especificar el modelo de datos
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: Optional[bool] = False


# Creando un endpoint que obtenga todas las pubicaciones
@app.get("/get-posts")
def getPosts():
    return publicaciones


# Creando endpoint para guardar publicaciones
@app.post("/save-post")
def save_post(post: Post):
    post.id = str(uuid())
    publicaciones.append(post.dict())
    return publicaciones[-1]


