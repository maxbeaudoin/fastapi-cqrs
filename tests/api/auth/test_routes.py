import pytest

from api.health.models.health_status import HealthStatus

@pytest.mark.asyncio
async def test_auth_check_success(client, mock_mediator, override_verify_api_key):
    mock_mediator.send.return_value = None

    response = client.post("/auth/check")
    
    mock_mediator.send.assert_called_once()

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_auth_check_failure(client):
    response = client.post("/auth/check")
    
    assert response.status_code == 401