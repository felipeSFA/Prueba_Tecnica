from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

tareas = Table(
    "tareas",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "titulo",
        String(255),
    ),
    Column("descripcion", String(255)),
    Column("fechaDeCreacion", DateTime()),
    Column("fechaDeModificacion", DateTime()),
)

meta.create_all(engine)