from strategy import Sorter, BubbleSortStrategy, QuickSortStrategy
from chain_of_responsibility import (Request, RequestType,
                                     ConcreteHandlerA, ConcreteHandlerB)
from iterator import Playlist
from proxy import DatabaseProxy
from adapter import ExternalLogger, LoggerAdapter
from bridge import Monitor, Printer, TextOutput, ImageOutput


def demo_strategy():
    print("         Strategy")
    sorter = Sorter()
    data = [5, 3, 8, 4, 2]
    sorter.set_strategy(BubbleSortStrategy())
    print(sorter.sort_array(data))
    sorter.set_strategy(QuickSortStrategy())
    print(sorter.sort_array(data))


def demo_chain():
    print("\n    Chain of Responsibility")
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next_handler(handler_b)
    for t in (RequestType.TYPE_A, RequestType.TYPE_B, RequestType.TYPE_C):
        handled = handler_a.handle_request(Request(t))
        if not handled:
            print(f"{t.name}: никто не обработал запрос")


def demo_iterator():
    print("\n                  Iterator")
    playlist = Playlist(["Song 1", "Song 2", "Song 3"])
    it = playlist.iterator()
    while it.has_next():
        print("forward:", it.next())
    it = playlist.reverse_iterator()
    while it.has_next():
        print("reverse:", it.next())
    print("for-цикл:", [s for s in playlist])
    try:
        it.next()
    except IndexError as e:
        print("Ошибка за пределами коллекции:", e)


def demo_proxy():
    print("\n                Proxy")
    DatabaseProxy(False).query("SELECT * FROM users")
    DatabaseProxy(True).query("SELECT * FROM users")


def demo_adapter():
    print("\n               Adapter")
    logger = LoggerAdapter(ExternalLogger())
    logger.log("This is a test message.")


def demo_bridge():
    print("\n                Bridge")
    monitor, printer = Monitor(), Printer()
    TextOutput(monitor).render("Hello, world!")
    TextOutput(printer).render("Hello, world!")
    ImageOutput(monitor).render("101010101")


if __name__ == "__main__":
    demo_strategy()
    demo_chain()
    demo_iterator()
    demo_proxy()
    demo_adapter()
    demo_bridge()