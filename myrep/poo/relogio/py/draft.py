class Watch:
    def __init__(self, hour: int, minute: int, seconds: int):
        self.__hour    = self.setHour(hour);
        self.__minute  = self.setMinute(minute);
        self.__seconds = self.setSeconds(seconds);

    def __str__(self) -> str:
        return f"{self.getHour()}:{self.getMinute()}:{self.getSeconds()}";
    
    # Métodos de busca

    def getHour(self) -> str:
        return f"{self.__hour:.2d}";

    def getMinute(self) -> str:
        return f"{self.__minute:.2d}";

    def getSeconds(self) -> str:
        return f"{self.__seconds:.2d}";

    # Métodos mutantes

    def setHour(self, value):
        if value < 0 or value > 23:
            print("fail: hora invalida");
            return;

        self.__hour = value;
    
    def setMinute(self, value):
        if value < 0 or value > 59:
            print("fail: minuto invalido");
            return;

        self.__minute = value;
    
    def setSeconds(self, value):
        if value < 0 or value > 59:
            print("fail: segundo invalido");
            return;

        self.__minute = value;

    # Método incrementar tempo

    def nextScond(self):
        self.setSeconds(self.setSeconds + 1);

        if self.getSeconds() > 59:
            self.setSeconds(0);
            self.setMinute(self.getMinute() + 1);

        if self.getMinute() > 59:
            self.setMinute(0);
            self.setHour(self.getHour() + 1);

        if self.getHour() > 59:
            self.setHour(0);
            self.setMinute(0);
            self.setSeconds(0);

        return;

relogio = Watch(16, 59, 30);

print(relogio);