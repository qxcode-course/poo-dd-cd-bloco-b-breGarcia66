# Criando classe Notebook

class Notebook:
    def __init__(self):
        self.__ligado: bool = False;

    # método string
    def __str__(self) -> str:
        return f'status: {'ligado' if True else 'desligado'}';

    # método de acesso
    def getLigado(self) -> bool:
        return self.__ligado;

    # método de mutação
    def setLigado(self, value: bool):
        self.__ligado = value

    # métodos do objeto
    def ligar(self):
        if self.getLigado() == False:
            self.setLigado(True);
            print('notebook ligado');

        return;

    def desligar(self):
        if self.getLigado() == True:
            self.setLigado(False);
            print('notebook desligado');

        return;

    def usar(self, time: int):
        if self.getLigado() == False:
            print('erro: ligue o notebook primeiro');
            return;

        print(f'usando notebook por {time} minutos');


# Main

notebook: Notebook = Notebook();
print(notebook);
notebook.usar(10);

notebook.ligar();
print(notebook);
notebook.usar(10);

notebook.desligar();


