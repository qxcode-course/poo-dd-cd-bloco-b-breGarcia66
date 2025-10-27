# criand classe Lead

class Lead:
    
    # construtor
    def __init__(self, thickness: float = 0.0, hardness: str = '', size: int = 0):
        self.__thickness: float = thickness;
        self.__hardness: str = hardness;
        self.__size: int = size;
    # fim construtor

    # método string
    def __str__(self) -> str:
        return f'[{self.getThickness()}:{self.getHardness()}:{self.getSize()}]';
    # fim método string

    # método de acesso
    def getThickness(self) -> float:
        return self.__thickness;

    def getHardness(self) -> str:
        return self.__hardness;

    def getSize(self) -> int:
        return self.__size;
    # fim método de acesso

    # método mutante
    def setThickness(self, value: float):
        if value < 0:
            print('fail: calibre invalida');
            return;

        self.__thickness = value;

    def setHardness(self, value: str):
        availableHardnesses: list[str] = ['HB', '2B', '4B', '6B'];
        if value.upper() not in availableHardnesses:
            print('fail: dureza invalida');
            return;

        self.__hardness = value;

    def setSize(self, value: int):
        self.__size = value; 
    # fim método mutante

    # método do objeto
    def usagePerPage(self):
        match self.getHardness():
            case 'HB':
                return 1;
            
            case '2B':
                return 2

            case '4B':
                return 4;
            
            case '6B':
                return 6;

            case _:
                return;
    # fim método do objeto