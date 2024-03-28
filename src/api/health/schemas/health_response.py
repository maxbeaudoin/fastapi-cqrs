from pydantic import BaseModel

from ..models.health_status import HealthStatus

class HealthResponse(BaseModel):
    status: HealthStatus
