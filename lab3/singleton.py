import threading


class AppConfig:
    """Конфигурация приложения - единственная на всю программу."""

    _instance = None
    _lock = threading.Lock()  # защита от гонки при создании из нескольких потоков

    def __new__(cls):
        # double-checked locking: блокировка берётся только при первом создании
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._settings = {"language": "ru", "debug": False}  # инициализация один раз
                    cls._instance = instance
        return cls._instance

    @classmethod
    def get_instance(cls) -> "AppConfig":
        return cls()

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def set(self, key, value) -> None:
        self._settings[key] = value