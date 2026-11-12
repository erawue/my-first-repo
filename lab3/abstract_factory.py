from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self) -> None: ...


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> None: ...

class WindowsButton(Button):
    def paint(self) -> None:
        print("You have created a Windows button.")


class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created a Windows checkbox.")


class MacButton(Button):
    def paint(self) -> None:
        print("You have created a Mac button.")


class MacCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created a Mac checkbox.")

class LinuxButton(Button):
    def paint(self) -> None:
        print("You have created a Linux button.")


class LinuxCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created a Linux checkbox.")

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self._button = factory.create_button()
        self._checkbox = factory.create_checkbox()

    def paint(self) -> None:
        self._button.paint()
        self._checkbox.paint()