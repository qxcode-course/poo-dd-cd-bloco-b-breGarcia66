# criando carregador

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia;

    # método de string
    def __str__(self) -> str:
        return f'(Potência {self.__potencia})';
    # fim método de string

    # método de acesso
    def getPotenca(self) -> int:
        return self.__potencia;
    # fim método de acesso

    # método de mutação
    def setPotencia(self, value: int):
        if value < 0:
            print('erro: potência inválida para carregador');
            return;

        self.__potencia = value
    # fim método de mutação

    # metodo do objeto
    def mostrar(self):
        print(self);
    # fim método do objeto

# fim carregador