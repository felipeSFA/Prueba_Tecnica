from fastapi import APIRouter
from config.db import conn
from modelos.tareas import tareas
from schemas.tarea import Tarea, TareaCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select


from datetime import datetime

tarea = APIRouter()



@tarea.get(
    "/tareas",
    tags=["tareas"],
    response_model=List[Tarea],
    description="Obtener todas las Tareas",
)
def get_tareas():
    return conn.execute(tareas.select()).fetchall()


@tarea.get("/tareas/count", tags=["tareas"], response_model=TareaCount)
def get_tareas_count():
    result = conn.execute(select([func.count()]).select_from(tareas))
    return {"total": tuple(result)[0][0]}


@tarea.get(
    "/tareas/{id}",
    tags=["tareas"],
    response_model=Tarea,
    description="Obtener una sola tarea por su ID",
)
def get_tarea(id: str):
    return conn.execute(tareas.select().where(tareas.c.id == id)).first()


@tarea.post("/", tags=["tareas"], response_model=Tarea, description="Crear Una Nueva Tarea")
def create_tarea(tarea: Tarea):
    new_tarea = {"titulo": tarea.titulo, "descripcion": tarea.descripcion, "fechaDeCreacion": datetime.now(), "fechaDeModificacion": datetime.now()}
    #new_tarea["password"] = f.encrypt(tarea.password.encode("utf-8"))
    result = conn.execute(tareas.insert().values(new_tarea))
    return conn.execute(tareas.select().where(tareas.c.id == result.lastrowid)).first()
#def create_tarea(tarea: Tarea):
    #new_tarea = {"name": tarea.name, "email": tarea.email}
    #new_tarea["password"] = f.encrypt(tarea.password.encode("utf-8"))
    #result = conn.execute(tareas.insert().values(new_tarea))
    #return conn.execute(tareas.select().where(tareas.c.id == result.lastrowid)).first()


@tarea.put("/tareas/{id}", tags=["tareas"], response_model=Tarea, description="Actualizar una tarea por su ID")
def update_tarea(id: int, tarea: Tarea):
    conn.execute(
        tareas.update()
        .values(titulo=tarea.titulo, descripcion=tarea.descripcion, fechaDeModificacion = datetime.now())
        .where(tareas.c.id == id)
    )
    return conn.execute(tareas.select().where(tareas.c.id == id)).first()


@tarea.delete("/{id}", tags=["tareas"], status_code=HTTP_204_NO_CONTENT)
def delete_tarea(id: int):
    conn.execute(tareas.delete().where(tareas.c.id == id))
    return conn.execute(tareas.select().where(tareas.c.id == id)).first()