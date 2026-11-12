from abc import ABC, abstractmethod
from itertools import count

class Attacker(ABC):
    """То, что может атаковать другие юниты."""

    @abstractmethod
    def attack(self, unit: "Unit") -> None:
        """Наносит урон переданному юниту."""


class Moveable(ABC):
    """То, что может перемещаться по карте."""

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        """Перемещает объект в точку (x, y)."""


class GameObject(ABC):
    """Базовый класс всех игровых объектов."""

    _id_counter = count(1)  # общий генератор уникальных id

    def __init__(self, name: str, x: int = 0, y: int = 0):
        self._id = next(GameObject._id_counter)
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    @abstractmethod
    def describe(self) -> str:
        """Текстовое описание объекта (реализуют наследники)."""

    def __str__(self) -> str:
        return self.describe()


class Unit(GameObject, ABC):
    """Управляемое подразделение: у него есть здоровье."""

    def __init__(self, name: str, x: int, y: int, hp: float):
        super().__init__(name, x, y)
        self._hp = float(hp)

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0.0, self._hp - damage)

    def describe(self) -> str:
        state = "жив" if self.is_alive() else "мёртв"
        return (f"[{self.get_id()}] {self.get_name()} "
                f"({self._x}, {self._y}) HP={self._hp:g} - {state}")


class Archer(Unit, Attacker, Moveable):
    """Лучник: умеет атаковать и перемещаться."""

    def __init__(self, name: str, x: int, y: int,
                 hp: float = 50, damage: float = 10):
        super().__init__(name, x, y, hp)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.is_alive():
            print(f"{self.get_name()} мёртв и не может атаковать")
            return
        print(f"{self.get_name()} стреляет в {unit.get_name()} (-{self._damage:g})")
        unit.receive_damage(self._damage)

    def move(self, x: int, y: int) -> None:
        if not self.is_alive():
            print(f"{self.get_name()} мёртв и не может двигаться")
            return
        self._x, self._y = x, y



class Building(GameObject, ABC):
    """Постройка: может быть построена или ещё нет."""

    def __init__(self, name: str, x: int, y: int, built: bool = False):
        super().__init__(name, x, y)
        self._built = built

    def is_built(self) -> bool:
        return self._built

    def finish_construction(self) -> None:
        self._built = True

    def describe(self) -> str:
        state = "построено" if self._built else "строится"
        return f"[{self.get_id()}] {self.get_name()} ({self._x}, {self._y}) - {state}"


class Fort(Building, Attacker):
    """Крепость: стреляет из пушек по противникам."""

    def __init__(self, name: str, x: int, y: int,
                 built: bool = True, cannon_damage: float = 25):
        super().__init__(name, x, y, built)
        self._cannon_damage = cannon_damage

    def attack(self, unit: Unit) -> None:
        if not self.is_built():
            print(f"{self.get_name()} ещё не достроена, пушки не работают")
            return
        print(f"{self.get_name()} стреляет из пушек в {unit.get_name()} "
              f"(-{self._cannon_damage:g})")
        unit.receive_damage(self._cannon_damage)


class MobileHouse(Building, Moveable):
    """Дом на колёсах: постройка, которую можно перевезти."""

    def __init__(self, name: str, x: int, y: int, built: bool = True):
        super().__init__(name, x, y, built)

    def move(self, x: int, y: int) -> None:
        if not self.is_built():
            print(f"{self.get_name()} ещё не достроен, ехать нельзя")
            return
        self._x, self._y = x, y


MobileHome = MobileHouse  # имя из диаграммы
