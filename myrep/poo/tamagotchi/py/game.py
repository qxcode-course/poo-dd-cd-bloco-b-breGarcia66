from tamagochi import Tamagochi;

# criando classe Game

class Game:
    
    # construtor
    def __init__(self, bixo: Tamagochi = None):
        self.__bixo: Tamagochi | None = bixo;
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
    def play(self):
        if self.getBixo().isAlive() is False:
            print('fail: pet esta morto');
            return;

        self.getBixo().setEnergy(self.getBixo().getEnergy() - 2);
        self.getBixo().setClean(self.getBixo().getClean() - 3);
        self.getBixo().setAge(self.getBixo().getAge() + 1);

        if self.getBixo().getEnergy() <= 0:
            print('fail: pet morreu de fraqueza');
            self.getBixo().setEnergy(0);
            return;

        if self.getBixo().getClean() <= 0:
            print('fail: pet morreu de sujeira');
            self.getBixo().setClean(0);            
            return;

    def sleep(self):
        if self.getBixo().isAlive() is False:
            print('fail: pet esta morto');
            return;

        if self.getBixo().getEnergy() > (self.getBixo().getEnergyMax() - 5):
            print('fail: nao esta com sono');
            return;
        
        turnosDeSono = self.getBixo().getEnergyMax() - self.getBixo().getEnergy();
        self.getBixo().setAge(self.getBixo().getAge() + turnosDeSono);

        self.getBixo().setEnergy(self.getBixo().getEnergyMax());

    def shower(self):
        if self.getBixo().isAlive() is False:
            print('fail: pet esta morto');
            return;

        if self.getBixo().getClean() == self.getBixo().getCleanMax():
            print('fail: não esta sujo');
            return; 

        self.getBixo().setClean(self.getBixo().getCleanMax());
        self.getBixo().setEnergy(self.getBixo().getEnergy() - 3);
        self.getBixo().setAge(self.getBixo().getAge() + 2);
        
    # fim método o objeto
    