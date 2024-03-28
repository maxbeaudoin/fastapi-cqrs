from fastapi import FastAPI

from .routes import router 

def include_health_router(app: FastAPI):
    app.include_router(router)