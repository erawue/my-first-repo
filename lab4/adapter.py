from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None: ...


class ExternalLogger:
    def log_message(self, msg: str) -> None:
        print(f"External log: {msg}")


class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self._external_logger = external_logger

    def log(self, message: str) -> None:
        self._external_logger.log_message(message)