from pessoa import Pessoa;

# criando classe MotoUber

class MotoUber:

    # construtor
    def __init__(self, custo: int = 0, motorista: Pessoa = None, passageiro: Pessoa = None):
        self.__custo = custo;
        self.__motorista = motorista;
        self.__passageiro = passageiro;
    # fim construtor

    # método string
    def __str__(self) -> str:
        return f'Cost: {self.getCusto()}, Driver: {self.getMotorista() if self.getMotorista() is not None else None}, Passenger: {self.getPassageiro() if self.getPassageiro() is not None else None}';
    # fim método string

    # método de acesso
    def getCusto(self) -> int:
        return self.__custo;

    def getMotorista(self) -> Pessoa | None:
        return self.__motorista;

    def getPassageiro(self) -> Pessoa | None:
        return self.__passageiro;
    # fim método de acesso

    # método mutante
    def setCusto(self, valor: int):
        if valor < 0:
            print('fail: valor de custo inválido');
            return;

        self.__custo = valor;

    def setMotorista(self, obj: Pessoa):
        self.__motorista = obj;

    def setPassageiro(self, obj: Pessoa):
        if self.getMotorista() is None:
            print('fail: nao pode ter passageio sem motorista');
            return;

        self.__passageiro = obj;
    # fim método mutante

    # método do objeto
    def descerPassageiro(self) -> Pessoa | None:
        if self.getPassageiro() is None:
            print('fail: nao tem passageiros para descer');
            return;

        oldPassageiro = self.getPassageiro();

        if self.getCusto() > self.getPassageiro().getDinheiro():
            print('fail: Passenger does not have enough money');

            self.getPassageiro().setDinheiro(0);
            self.getMotorista().setDinheiro(self.getMotorista().getDinheiro() + self.getCusto());
            self.setCusto(0);

            self.setPassageiro(None);            
            return oldPassageiro;

        self.getPassageiro().setDinheiro(self.getPassageiro().getDinheiro() - self.getCusto());
        self.getMotorista().setDinheiro(self.getMotorista().getDinheiro() + self.getCusto());
        self.setCusto(0)

        self.setPassageiro(None);
        return oldPassageiro;

    def corrida(self, distancia):
        if distancia < 0:
            print('fail: distancia invalida');
            return;
    
        if self.getPassageiro() is None:
            print('fail: sem passageiro');
            return;

        self.setCusto(self.getCusto() + distancia);
    # fim método do objeto