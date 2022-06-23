from fastapi import FastAPI
from routes.tareas import tarea
from routes.auth import auth_routes
from config.openapi import tags_metadata
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

app = FastAPI(
    title="Tareas API",
    description="API para el proceso de seleccion DIGIWORLD",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

load_dotenv()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarea)
app.include_router(auth_routes, prefix="/auth")
