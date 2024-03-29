from typing import Type, TypeVar, Generic

from .request_handler import QueryHandler

TQuery = TypeVar('TQuery')
TResult = TypeVar('TResult')

class Mediator(Generic[TQuery, TResult]):
    def __init__(self, handlers: dict[Type[TQuery], Type['QueryHandler[TQuery, TResult]']]):
        self.handlers = handlers

    async def send(self, query: TQuery) -> TResult:
        handler = self.handlers[type(query)]
        return await handler.handle(query)