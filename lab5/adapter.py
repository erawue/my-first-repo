# Новый интерфейс умного дома
class SmartHomeInterface:
    def execute_command(self, command):
        pass

# Старый пульт от телевизора (несовместимый интерфейс)
class OldTVRemote:
    def press_button(self, button_code):
        print(f"(OldTVRemote) Нажата кнопка с кодом {button_code}")
        return True

# Адаптер: переводит команды умного дома в нажатия кнопок старого пульта
class RemoteAdapter(SmartHomeInterface):
    def __init__(self, old_remote):
        self.old_remote = old_remote

    def execute_command(self, command):
        # Переводим текстовую команду в код кнопки
        if command == "POWER":
            code = 101
        elif command == "VOLUME_UP":
            code = 102
        else:
            print("Неизвестная команда")
            return False
        
        return self.old_remote.press_button(code)

# Клиентский код
def control_device(device, command):
    print(f"Отправка команды: {command}")
    success = device.execute_command(command)
    print("Успешно" if success else "Ошибка")

if __name__ == "__main__":
    old_remote = OldTVRemote()
    adapter = RemoteAdapter(old_remote)

    control_device(adapter, "POWER")
    control_device(adapter, "VOLUME_UP")