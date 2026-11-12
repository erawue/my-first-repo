# Интерфейс способа оповещения
class Notifier:
    def notify(self, message):
        pass

# Конкретные реализации оповещений
class PhoneNotifier(Notifier):
    def notify(self, message):
        print(f"📱 Уведомление на телефон: {message}")

class SpeakerNotifier(Notifier):
    def notify(self, message):
        print(f"🔊 Голосовое оповещение: {message}")

# Базовый датчик (Абстракция)
class Sensor:
    def __init__(self, notifier):
        self.notifier = notifier # Мост к реализации оповещения

    def check(self):
        data = self.read_data()
        self.notifier.notify(data)

    def read_data(self):
        pass

# Расширенные датчики
class TemperatureSensor(Sensor):
    def read_data(self):
        return "Температура в комнате упала до 18°C"

class HumiditySensor(Sensor):
    def read_data(self):
        return "Влажность достигла 80%"

if __name__ == "__main__":
    # Датчик температуры отправляет данные на телефон
    temp_sensor = TemperatureSensor(PhoneNotifier())
    temp_sensor.check()

    # Датчик влажности оповещает через колонку
    hum_sensor = HumiditySensor(SpeakerNotifier())
    hum_sensor.check()