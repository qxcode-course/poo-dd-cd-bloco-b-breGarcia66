from person import Person;

# criando classe motocycle

class MotoCycle:
    def __init__(self, person: Person = None, power: int = 1, time: int = None):
        self.__person: Person | None = person;
        self.__power = power;
        self.__time = time;

    def __str__(self):
        return f"power:"

    def getPerson(self) -> Person | None:
        return self.__person;

    def getPower(self) -> int:
        return self.__power;

    def getTime(self) -> int:
        return  self.__time;