from fastapi import APIRouter, Response, Depends

from common.dependencies import get_mediator
from common.mediator import Mediator
from services.auth import verify_api_key
from .commands.check_auth_command import CheckAuthCommand

router = APIRouter()

@router.post("/auth/test", dependencies=[Depends(verify_api_key)])
async def health_check(mediator: Mediator = Depends(get_mediator)):
    await mediator.send(CheckAuthCommand())
    return Response(status_code=200)
    