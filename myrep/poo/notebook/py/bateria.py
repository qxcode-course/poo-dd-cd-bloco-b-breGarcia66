# Criando classe Bateria
class Bateria:
    def __init__(self, capacidade: int):
        self.__carga: int = capacidade;
        self.__capacidade: int = capacidade;

    # Método de string
    def __str__(self):
        return f"({self.getCarga()}/{self.getCapacidade()})";

    # Métodos de acesso
    def getCarga(self) -> int:
        return self.__carga;

    def getCapacidade(self) -> int:
        return self.__capacidade;
    
    # Métodos de mutações
    def setCarga(self, value):
        self.__carga += value;
          
        if self.getCarga() > self.getCapacidade():
            self.__carga = self.getCapacidade();

    def setCapacidade(self, value):
        if value < 0:
            print('erro: capacidade de bateria inválida');
            return;

        self.__capacidade = value;

    # método do objeto
    def mostrar(self):
        print(self);

# Fim Bateria
