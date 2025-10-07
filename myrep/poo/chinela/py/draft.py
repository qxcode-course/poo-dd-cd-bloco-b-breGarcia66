class Chinelo:
    def __init__(self):
        self.__tamanho = 0;

    def getTamanho(self) -> int:
        return self.__tamanho;

    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50 or valor % 2 != 0:
            print("erro: valor invalido");
            return;

        self.__tamanho = valor;

chinelo = Chinelo();
while chinelo.getTamanho() == 0:
    chinelo.setTamanho(int(input("Tamanho do chinelo:\n")));

print(f"O seu chinelo tem o tamanho {chinelo.getTamanho()}");