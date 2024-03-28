import pytest
from src.api.health.models.health_status import HealthStatus
from src.api.health.queries.health_check_query import HealthCheckQuery, HealthCheckQueryHandler

@pytest.mark.asyncio
async def test_health_check_query_handler():
    # Arrange
    query = HealthCheckQuery()
    handler = HealthCheckQueryHandler()

    # Act
    result = await handler.handle(query)

    # Assert
    assert result == HealthStatus.OK