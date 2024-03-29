from fastapi import FastAPI

from api.auth import include_auth_router
from api.health import include_health_router

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

def create_app():
    app = FastAPI()
    include_auth_router(app)
    include_health_router(app)
    return app
