from person import Person;

# criando classe motocycle

class MotoCycle:

    # construtor
    def __init__(self, person: Person = None, power: int = 1, time: int = 0):
        self.__person: Person | None = person;
        self.__power = power;
        self.__time = time;
    # fim construtor

    # método string
    def __str__(self):
        return f"power:{self.getPower()}, time:{self.getTime()}, person:({self.getPerson() if self.getPerson() is not None else 'empty'})";
    # fim método string

    # metodo de acesso
    def getPerson(self) -> Person | None:
        return self.__person;

    def getPower(self) -> int:
        return self.__power;

    def getTime(self) -> int:
        return  self.__time;
    # fim método de acesso

    # método mutante
    def setPerson(self, person: Person):
        self.__person = person;

    def setPower(self, value: int):
        if value < 0:
            print('fail: potencia de motoca inválida');
            return;
    
        self.__power = value;

    def setTime(self, value):
        self.__time = value;
    # fim método mutante

    # método próprio do objeto
    def inserir(self, pessoa: Person) -> bool:
        if self.getPerson() is not None:
            print('fail: busy motorcycle');
            return False;

        else:
            self.setPerson(pessoa);
            return True;

    def remover(self) -> Person | None:
        if self.getPerson() is None:
            print('fail: empty motorcycle');
            return;
        
        oldPessoa = self.getPerson();
        self.setPerson(None);
        return oldPessoa;

    def buyTime(self, value: int):
        if value < 0:
            print('fail: valor invalido para comprar tempo');
            return;

        self.setTime(self.getTime() + value);

    def drive(self, time: int):
        if self.getTime() == 0:
            print('fail: buy time first');
            return;

        if self.getPerson() is None:
            print('fail: empty motorcycle')
            return;

        if self.getPerson().getAge() > 10:
            print('fail: too old to drive');
            return;

        if time >= self.getTime():
            print(f'fail: time finished after {self.getTime()} minutes');
            self.setTime(0);
            return;

        self.setTime(self.getTime() - time);

    def honk(self):
        powerHonk = 'e' * self.getPower();
        print(f'P{powerHonk}m');
    # fim método próprio do objeto
