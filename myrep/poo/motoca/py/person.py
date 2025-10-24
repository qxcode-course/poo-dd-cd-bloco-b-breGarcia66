# criando classe person

class Person:

    # construtor
    def __init__(self, age: int = 0, name: str = ''):
        self.__age = age;
        self.__name = name;
    # fim construtor

    # método string
    def __str__(self):
        return f"{self.getName()}:{self.getAge()}";
    # fim método string

    # método de acesso
    def getAge(self) -> int:
        return self.__age;

    def getName(self) -> str:
        return self.__name;
    # fim método de acesso

    # método mutante
    def setAge(self, value):
        if value < 0:
            print('fail: idade invalida');
            return;

        self.__age = value;

    def setName(self, value):
        self.__name = value;
    # fim método mutante