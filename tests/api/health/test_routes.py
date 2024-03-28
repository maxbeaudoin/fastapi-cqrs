import pytest

from api.health.models.health_status import HealthStatus

@pytest.mark.asyncio
async def test_health_check_success(client, mock_mediator):
    mock_mediator.send.return_value = HealthStatus.OK

    response = client.get("/health")
    
    mock_mediator.send.assert_called_once()

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

@pytest.mark.asyncio
async def test_health_check_failure(client, mock_mediator):
    mock_mediator.send.return_value = HealthStatus.ERROR

    response = client.get("/health")
    
    mock_mediator.send.assert_called_once()
    assert response.status_code == 503