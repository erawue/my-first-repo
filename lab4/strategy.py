from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> list[int]:
        """Возвращает новый отсортированный список."""


class BubbleSortStrategy(SortingStrategy):
    def sort(self, array: list[int]) -> list[int]:
        print("Sorting using Bubble Sort")
        result = list(array)
        n = len(result)
        for i in range(n):
            for j in range(n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result


class QuickSortStrategy(SortingStrategy):
    def sort(self, array: list[int]) -> list[int]:
        print("Sorting using Quick Sort")
        return self._quick(list(array))

    def _quick(self, items: list[int]) -> list[int]:
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return self._quick(left) + middle + self._quick(right)


class Sorter:
    def __init__(self, strategy: SortingStrategy | None = None):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy) -> None:
        self._strategy = strategy

    def sort_array(self, array: list[int]) -> list[int]:
        if self._strategy is None:
            raise RuntimeError("Стратегия сортировки не задана")
        return self._strategy.sort(array)