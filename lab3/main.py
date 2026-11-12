import threading

from singleton import AppConfig
from factory_method import FileLoggerFactory, ConsoleLoggerFactory
from abstract_factory import Application, WindowsFactory, MacFactory, LinuxFactory
from builder import HawaiianPizzaBuilder, PepperoniPizzaBuilder, PizzaDirector


def demo_singleton():
    print("            Singleton")
    a = AppConfig()
    b = AppConfig.get_instance()
    a.set("debug", True)
    print("a is b:", a is b)
    print("b.get('debug'):", b.get("debug"))

    ids = set()

    def worker():
        ids.add(id(AppConfig()))

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Разных экземпляров из 20 потоков:", len(ids))


def demo_factory_method():
    print("\n         Factory Method")
    for factory in (FileLoggerFactory(), ConsoleLoggerFactory()):
        factory.log_message("Hello, patterns!")


def demo_abstract_factory():
    print("\n        Abstract Factory")
    for factory in (WindowsFactory(), MacFactory(), LinuxFactory()):
        Application(factory).paint()


def demo_builder():
    print("\n                           Builder")
    for builder in (HawaiianPizzaBuilder(), PepperoniPizzaBuilder()):
        PizzaDirector(builder).construct_pizza()
        print(builder.get_result())


if __name__ == "__main__":
    demo_singleton()
    demo_factory_method()
    demo_abstract_factory()
    demo_builder()