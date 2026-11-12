from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self) -> str:
        return (f"Pizza(dough='{self.dough}', sauce='{self.sauce}', "
                f"topping='{self.topping}')")

class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self) -> None: ...

    @abstractmethod
    def build_sauce(self) -> None: ...

    @abstractmethod
    def build_topping(self) -> None: ...

    @abstractmethod
    def get_result(self) -> Pizza: ...


class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def build_dough(self) -> None:
        self._pizza.dough = "cross"

    def build_sauce(self) -> None:
        self._pizza.sauce = "mild"

    def build_topping(self) -> None:
        self._pizza.topping = "ham+pineapple"

    def get_result(self) -> Pizza:
        return self._pizza


class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def build_dough(self) -> None:
        self._pizza.dough = "thin"

    def build_sauce(self) -> None:
        self._pizza.sauce = "spicy"

    def build_topping(self) -> None:
        self._pizza.topping = "pepperoni+cheese"

    def get_result(self) -> Pizza:
        return self._pizza

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def construct_pizza(self) -> None:
        self._builder.build_dough()
        self._builder.build_sauce()
        self._builder.build_topping()