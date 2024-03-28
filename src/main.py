from fastapi import FastAPI

from api.health import include_health_router

def create_app():
    app = FastAPI()
    include_health_router(app)
    return app
