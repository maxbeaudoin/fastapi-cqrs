from .mediator import Mediator

def get_mediator() -> Mediator:
    from api.auth.commands import CheckAuthCommand, CheckAuthCommandHandler
    from api.health.queries import HealthCheckQuery, HealthCheckQueryHandler

    handlers = {
        CheckAuthCommand: CheckAuthCommandHandler(),
        HealthCheckQuery: HealthCheckQueryHandler()
    }
    return Mediator(handlers)