from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> None: ...


class RealDatabase(Database):
    def query(self, sql: str) -> None:
        print(f"Executing query: {sql}")


class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self._real_database: RealDatabase | None = None  # ленивая инициализация
        self._has_access = has_access

    def query(self, sql: str) -> None:
        if not self._has_access:
            print("Access denied. Query cannot be executed.")
            return
        if self._real_database is None:
            self._real_database = RealDatabase()
        self._real_database.query(sql)