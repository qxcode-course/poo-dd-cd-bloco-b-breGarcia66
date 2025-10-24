# criando classe Tamagochi

class Tamagochi:
    
    # contrutuor
    def __init__(self, energyMax: int, cleanMax:int):
        self.__energyMax: int = energyMax;
        self.__energy: int = energyMax; 
        self.__cleanMax: int = cleanMax;
        self.__clean: int = cleanMax;    
        self.__age: int = 0;
        self.__alive: bool = True;
    # fim contrutor

    # método string
    def __str__(self) -> str:
        return f'E:{self.getEnergy()}/{self.getEnergyMax()}, L:{self.getClean()}/{self.getCleanMax()}, I:{self.getAge()}';
    # fim métdodo string

    # método de acesso
    def getEnergyMax(self) -> int:
        return self.__energyMax;
    
    def getEnergy(self) -> int:
        return self.__energy;
    
    def getCleanMax(self) -> int:
        return self.__cleanMax;
    
    def getClean(self) -> int:
        return self.__clean;

    def getAge(self) -> int:
        return self.__age;

    def isAlive(self) -> bool:
        return self.__alive;
    # fim método de acesso

    # método mutante
    def setEnergy(self, value: int):
        if value < 0:
            print('fail: valor invalido');
            return;

        self.__energy = value;

    def setClean(self, value: int):
        if value < 0:
            print('fail: valor invalido');
            return;
        
        self.__clean = value;

    def setAge(self, value: int):
        if value < 0:
            print('fail: valor invalido');
            return;
        
        self.__age = value;

    def setAlive(self, value: bool):
        self.__alive = value;
    # fim método mutante