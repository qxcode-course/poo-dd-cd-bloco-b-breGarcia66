# criando classe Pessoa

class Pessoa:
    # construtor
    def __init__(self, nome: str = '', dinheiro: int = 0):
        self.__nome = nome;
        self.__dinheiro = dinheiro;
    # fim construtor

    # método string
    def __str__(self) -> str:
        return f'{self.getNome()}:{self.getDinheiro()}';
    # fim método string

    # método de acesso
    def getNome(self) -> str:
        return self.__nome;

    def getDinheiro(self) -> int:
        return self.__dinheiro;
    # fim método de acesso

    # método mutante
    def setNome(self, nome: str):
        self.__nome = nome;

    def setDinheiro(self, valor: int):
        self.__dinheiro = valor;
    # fim método mutante
