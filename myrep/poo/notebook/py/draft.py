# Criando classe Notebook

class Notebook:
    def __init__(self):
        self.__ligado: bool = False;
        self.__bateria: Bateria | None = None;

    # método string
    def __str__(self) -> str:
        return f'status: {'ligado' if True else 'desligado'}';

    # método de acesso
    def getLigado(self) -> bool:
        return self.__ligado;

    def getBateria(self) -> Bateria | None:

    # método de mutação
    def setLigado(self, value: bool):
        self.__ligado = value

    # métodos do objeto
    def ligar(self):
        if self.__bateria.getCarga() == 0:
            print('nao foi possivel ligar');
            return;
    
        self.setLigado(True);

    def desligar(self):
        if self.getLigado() == True:
            self.setLigado(False);
            print('notebook desligado');

    def usar(self, time: int):
        if self.getLigado() == False:
            print('erro: ligue o notebook primeiro');
            return;

        if time > self.__bateria.getCarga():

        print(f'usando notebook por {time} minutos');

# Criando classe Bateria
class Bateria:
    def __init__(self, capacidade: int):
        self.__carga: int = capacidade;
        self.__capacidade: int = capacidade;

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
        if value > 0:
            self.__capacidade = value;
            return;

        print('capacidade de bateria inválida');


# Main

notebook: Notebook = Notebook();
print(notebook);
notebook.usar(10);

notebook.ligar();
print(notebook);
notebook.usar(10);

notebook.desligar();


