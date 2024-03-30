from fastapi import FastAPI

from .routes import router 

def include_auth_router(app: FastAPI):
    app.include_router(router, tags=["auth"])