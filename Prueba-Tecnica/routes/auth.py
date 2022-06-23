from fastapi import APIRouter, Header
from schemas.tarea import Usuario
from functions.functions_jwt import validate_token, write_token
from fastapi.responses import JSONResponse
from config.db import conn
from modelos.usuario import usuarios
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

from datetime import datetime

auth_routes = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)



@auth_routes.post("/register", tags=["users"], response_model=Usuario, description="Crear un nuevo Usuario")
def create_user(user: Usuario):
    new_user = {"username": user.username, "email": user.email, "token": write_token(user.dict()), "fechaDeCreacion": datetime.now(), "fechaDeModificacion": datetime.now()}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))

    result = conn.execute(usuarios.insert().values(new_user))
    return conn.execute(usuarios.select().where(usuarios.c.id == result.lastrowid)).first()
    


@auth_routes.post("/login")
def login(user: Usuario):
    #print(user.dict())
    if user.username != "":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "Usuario no Encontrado"}, status_code=404)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)