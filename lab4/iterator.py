from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class AbstractIterator(ABC, Generic[T]):
    @abstractmethod
    def has_next(self) -> bool: ...

    @abstractmethod
    def next(self) -> T: ...


class ArrayIterator(AbstractIterator[T]):
    def __init__(self, items: list[T]):
        self._items = items
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._items)

    def next(self) -> T:
        if not self.has_next():
            raise IndexError("Больше элементов нет")
        item = self._items[self._position]
        self._position += 1
        return item


class ReverseIterator(AbstractIterator[T]):
    def __init__(self, items: list[T]):
        self._items = items
        self._position = len(items) - 1

    def has_next(self) -> bool:
        return self._position >= 0

    def next(self) -> T:
        if not self.has_next():
            raise IndexError("Больше элементов нет")
        item = self._items[self._position]
        self._position -= 1
        return item


class Playlist(Generic[T]):
    def __init__(self, items: list[T]):
        self._items = list(items)

    def iterator(self) -> AbstractIterator[T]:
        return ArrayIterator(self._items)

    def reverse_iterator(self) -> AbstractIterator[T]:
        return ReverseIterator(self._items)

    def __iter__(self):
        return iter(self._items)