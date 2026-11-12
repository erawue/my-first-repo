from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None: ...


class FileLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to file: {message}")


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to console: {message}")


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        """Фабричный метод."""

    def log_message(self, message: str) -> None:
        logger = self.create_logger()  # работаем только с интерфейсом Logger
        logger.log(message)


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()