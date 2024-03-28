from .mediator import Mediator

def get_mediator() -> Mediator:
    from api.health.queries import HealthCheckQuery, HealthCheckQueryHandler

    handlers = {HealthCheckQuery: HealthCheckQueryHandler()}
    return Mediator(handlers)