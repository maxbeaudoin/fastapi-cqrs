from infrastructure.auth import verify_api_key
import pytest
from starlette.testclient import TestClient
from unittest.mock import AsyncMock

from infrastructure.dependencies import get_mediator
from infrastructure.mediator import Mediator
from main import create_app

@pytest.fixture(scope='module')
def app():
    return create_app()

@pytest.fixture(scope='module')
def client(app):
    return TestClient(app)

@pytest.fixture(scope='function')
def mock_mediator(app):
    mock_mediator = AsyncMock(spec=Mediator)
    app.dependency_overrides[get_mediator] = lambda: mock_mediator
    yield mock_mediator
    del app.dependency_overrides[get_mediator]

@pytest.fixture(scope='function')
def override_verify_api_key(app):
    app.dependency_overrides[verify_api_key] = lambda: "api_key"
    yield
    del app.dependency_overrides[verify_api_key]