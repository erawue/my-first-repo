from game_objects import Archer, Fort, MobileHouse, GameObject, Attacker, Moveable

def main():
    archer = Archer("Робин", 1, 1)
    enemy = Archer("Враг", 5, 5, hp=30)
    fort = Fort("Форт Нокс", 10, 10)
    house = MobileHouse("Караван", 3, 3, built=False)

    objects: list[GameObject] = [archer, enemy, fort, house]
    print("          Объекты        ")
    for obj in objects:
        print(obj)

    print("\n          Бой        ")
    archer.attack(enemy)
    fort.attack(enemy)          # 30 - 10 - 25 -> враг погибает
    print(enemy)
    enemy.attack(archer)        # мёртвый не атакует

    print("\n          Движение        ")
    archer.move(4, 4)
    house.move(0, 0)            # не достроен
    house.finish_construction()
    house.move(0, 0)
    print(archer)
    print(house)

    print("\nПолиморфизм по интерфейсам")
    for obj in objects:
        roles = []
        if isinstance(obj, Attacker):
            roles.append("Attacker")
        if isinstance(obj, Moveable):
            roles.append("Moveable")
        print(f"{obj.get_name()}: {', '.join(roles) or '-'}")

    try:
        GameObject("x")
    except TypeError as e:
        print("\nGameObject абстрактный:", e)


if __name__ == "__main__":
    main()
