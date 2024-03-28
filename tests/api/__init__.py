from unittest.mock import AsyncMock
from fastapi.testclient import TestClient

from src.common.dependencies import get_mediator
from src.common.mediator import Mediator
from src.main import create_app


def create_test_client(app = create_app()):
    client = TestClient(app)
    return client