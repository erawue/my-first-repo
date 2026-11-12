# Общий интерфейс для устройства
class SmartDevice:
    def turn_on(self):
        pass

# Реальное устройство
class RealLamp(SmartDevice):
    def __init__(self, name):
        self.name = name
        # Имитация долгой инициализации (подключение к Wi-Fi)
        print(f"[RealLamp] Подключение к лампе '{name}'... (долго)")

    def turn_on(self):
        print(f"[RealLamp] Лампа '{self.name}' включена.")

# Прокси: ленивая загрузка (включаем только при необходимости)
class LampProxy(SmartDevice):
    def __init__(self, name):
        self.name = name
        self._real_lamp = None

    def turn_on(self):
        # Создаем реальный объект только при первом вызове
        if self._real_lamp is None:
            self._real_lamp = RealLamp(self.name)
        self._real_lamp.turn_on()

if __name__ == "__main__":
    print("Создаю прокси для лампы (она еще не подключена)")
    lamp = LampProxy("Гостиная")
    
    print("\nПервое включение - идет подключение")
    lamp.turn_on()
    
    print("\nВторое включение - уже подключено")
    lamp.turn_on()