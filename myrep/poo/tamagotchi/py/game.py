from tamagochi import Tamagochi;

# criando classe Game

class Game:
    
    # construtor
    def __init__(self, bixo: Tamagochi):
        self.__bixo: Tamagochi = bixo;
    # fim construtor

    # método string
    def __str__(self) -> str:
        return f'{self.getBixo()}';
    # fim método string

    # método de acesso
    def getBixo(self) -> Tamagochi | None:
        return self.__bixo;
    # fim método de acesso

    # método mutante
    def setBixo(self, obj: Tamagochi):
        self.__bixo = obj;
    # fim método mutante

    # método do objeto
    
    # fim método o objeto
    