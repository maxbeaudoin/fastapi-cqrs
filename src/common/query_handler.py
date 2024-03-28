from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TQuery = TypeVar('TQuery')
TResult = TypeVar('TResult')

class QueryHandler(ABC, Generic[TQuery, TResult]):
    @abstractmethod
    async def handle(self, query: TQuery) -> TResult:
        pass