class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class Archer:
    def __init__(self, name, health, num_arrows):
        pass

    def shoot(self, target):
        pass
