from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

usuarios = Table(
    "usuarios",
    meta,
    Column("id", Integer, primary_key=True),
    Column("username",String(255),),
    Column("email",String(255),),
    Column("password",String(255),),
    Column("token", String(255)),
    Column("fechaDeCreacion", DateTime()),
    Column("fechaDeModificacion", DateTime()),
)

meta.create_all(engine)