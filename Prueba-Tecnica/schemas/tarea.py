from typing import Optional
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel, EmailStr

class Tarea(BaseModel):
    id: Optional[int]
    titulo: str
    descripcion: str
    fechaDeCreacion: Optional[datetime]
    fechaDeModificacion: Optional[datetime]

class Usuario(BaseModel):
    id: Optional[int]
    username: str
    email: EmailStr
    password: str
    token: Optional[str]
    fechaDeCreacion: Optional[datetime]
    fechaDeModificacion: Optional[datetime]

class TareaCount(BaseModel):
    total: int