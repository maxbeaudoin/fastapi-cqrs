from fastapi import APIRouter, Response, Depends

from infrastructure.dependencies import get_mediator
from infrastructure.mediator import Mediator
from infrastructure.auth import verify_api_key
from .commands.check_auth_command import CheckAuthCommand

router = APIRouter()

@router.post("/auth/check", dependencies=[Depends(verify_api_key)])
async def health_check(mediator: Mediator = Depends(get_mediator)):
    await mediator.send(CheckAuthCommand())
    return Response(status_code=200)
    