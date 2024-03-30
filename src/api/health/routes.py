from fastapi import APIRouter, HTTPException, Depends

from infrastructure.dependencies import get_mediator
from infrastructure.mediator import Mediator
from .models import HealthStatus
from .schemas import HealthResponse
from .queries import HealthCheckQuery

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check(mediator: Mediator = Depends(get_mediator)):
    health_status = await mediator.send(HealthCheckQuery())
    if health_status == HealthStatus.OK:
        return HealthResponse(status=health_status)
    else:
        raise HTTPException(status_code=503, detail="Service Unavailable")
    