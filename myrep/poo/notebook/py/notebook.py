from bateria import Bateria;
from carregador import Carregador;

# Criando classe Notebook

class Notebook:
    def __init__(self):
        self.__ligado: bool = False;
        self.__bateria: Bateria | None = None;
        self.__carregador: Carregador | None = None;

    # método string
    def __str__(self) -> str:
        return f'msg: status: {'ligado' if self.getLigado() else 'desligado'}, bateria: {self.getBateria() if self.getBateria() is not None else 'nenhuma'}, carregador: {self.getCarregador() if self.getCarregador() is not None else 'desconectado'}';
    # fim método string

    # método de acesso
    def getLigado(self) -> bool:
        return self.__ligado;

    def getBateria(self) -> Bateria | None:
        return self.__bateria;

    def getCarregador(self) -> Carregador | None:
        return self.__carregador;
    # fim método de acesso

    # método de mutação
    def setLigado(self, value: bool):
        self.__ligado = value

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria;
    
    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador;
    # fim método de mutação

    # métodos do objeto
    def mostrar(self):
        print(self);

    def ligar(self):
        if self.getLigado() == True:
            print('erro: nao foi possivel ligar');
            return;
    
        if self.getCarregador() is not None:
            self.setLigado(True);
            print('msg: notebook ligado');
            return;
    
        if self.getBateria() is None:
            print('erro: notebook sem bateria e sem carregador');
            return;

        if self.getBateria().getCarga() == 0:
            print('erro: bateria sem carga');
            return;
    
    
        self.setLigado(True);
        print('msg: notebook ligado');

    def desligar(self):
        if self.getLigado() == True:
            self.setLigado(False);
            print('msg: notebook desligado');
    
    def rmBateria(self) -> Bateria | None:
        if self.getBateria() is None:
            print('erro: computador já está sem bateria');
            return;

        bateriaRetirada = self.getBateria();
        self.setBateria(None)
        print('msg: bateria removida')

        return bateriaRetirada;

    def usar(self, time: int):
        if self.getLigado() == False:
            print('erro: ligue o notebook primeiro');
            return;

        if time > self.__bateria.getCarga():
            print(f'msg: usando por {self.getBateria().getCarga()} minutos, notebook descarregou');
            self.getBateria().setCarga(-self.getBateria().getCarga());
            self.setLigado(False);
            return;
        
        if self.getCarregador() is not None:
            self.getBateria().setCarga(time * self.getCarregador().getPotenca());
            print(f'msg: usando notebook por {time} minutos');
            return;
        
        print(f'msg: usando notebook por {time} minutos');
        self.getBateria().setCarga(- time);

        if self.getBateria().getCarga() == 0:
            self.setLigado(False);

            



