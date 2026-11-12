from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def print(self, data: str) -> None: ...


class Monitor(Device):
    def print(self, data: str) -> None:
        print(f"Displaying on monitor: {data}")


class Printer(Device):
    def print(self, data: str) -> None:
        print(f"Printing to paper: {data}")

class Output(ABC):
    def __init__(self, device: Device):
        self._device = device  # это и есть «мост»

    @abstractmethod
    def render(self, data: str) -> None: ...


class TextOutput(Output):
    def render(self, data: str) -> None:
        self._device.print(f"Text: {data}")


class ImageOutput(Output):
    def render(self, data: str) -> None:
        self._device.print(f"Image: [Binary data: {data}]")