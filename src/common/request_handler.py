from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TRequest = TypeVar('TRequest')
TResult = TypeVar('TResult')

class _RequestHandler(ABC, Generic[TRequest, TResult]):
    @abstractmethod
    async def handle(self, request: TRequest) -> TResult:
        pass

class QueryHandler(_RequestHandler[TRequest, TResult]):
    pass

class CommandHandler(_RequestHandler[TRequest, TResult]):
    pass