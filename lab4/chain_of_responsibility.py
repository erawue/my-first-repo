from abc import ABC, abstractmethod
from enum import Enum


class RequestType(Enum):
    TYPE_A = "A"
    TYPE_B = "B"
    TYPE_C = "C"  # никем не обрабатывается


class Request:
    def __init__(self, request_type: RequestType):
        self._type = request_type

    def get_type(self) -> RequestType:
        return self._type


class Handler(ABC):
    def __init__(self):
        self._next_handler: "Handler | None" = None

    def set_next_handler(self, next_handler: "Handler") -> "Handler":
        self._next_handler = next_handler
        return next_handler  # позволяет строить цепочку: a.set_next(b).set_next(c)

    def handle_request(self, request: Request) -> bool:
        """True, если запрос кем-то обработан."""
        if self.can_handle(request):
            self.process(request)
            return True
        if self._next_handler is not None:
            return self._next_handler.handle_request(request)
        return False

    @abstractmethod
    def can_handle(self, request: Request) -> bool: ...

    @abstractmethod
    def process(self, request: Request) -> None: ...


class ConcreteHandlerA(Handler):
    def can_handle(self, request: Request) -> bool:
        return request.get_type() == RequestType.TYPE_A

    def process(self, request: Request) -> None:
        print("ConcreteHandlerA handled the request.")


class ConcreteHandlerB(Handler):
    def can_handle(self, request: Request) -> bool:
        return request.get_type() == RequestType.TYPE_B

    def process(self, request: Request) -> None:
        print("ConcreteHandlerB handled the request.")