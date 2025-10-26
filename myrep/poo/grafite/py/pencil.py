from lead import Lead;

# criand classe Pencil

class Pencil:

    # construtor
    def __init__(self, thickness: float = 0):
        self.__thickness: float = thickness;
        self.__tip: Lead | None = None;
    # fim construtor

    # método string
    def __str__(self) -> str:
        return f'calibre: {self.getThickness()}, grafite: {self.getTip() if self.getTip() is not None else 'null'}';
    # fim método string

    # método de acesso
    def getThickness(self) -> float:
        return self.__thickness;

    def getTip(self) -> Lead | None:
        return self.__tip;
    # fim metodo de acesso

    # método mutante
    def setThickness(self, value: float):
        if value < 0:
            print('fail: invlalid thickness');
            return;

    def setTip(self, obj: Lead):
        self.__tip = obj;
    # fim método mutante

    # método do objeto
    def hasGrafite(self) -> bool:
        if self.getTip() is None:
            return False;

        return True;

    def insert(self, lead: Lead) -> bool:
        if self.hasGrafite() is True:
            print('fail: ja existe grafite');
            return False;

        if self.getThickness() != lead.getThickness():
            print('fail: calibre incompativel');
            return False;

        self.setTip(lead);
        return True;

    def remove(self) -> Lead | None:
        if self.getTip is None:
            print('fail: ja esta sem grafite');    
            return;

        oldTip: Lead = self.getTip();
        self.setTip(None);

        return oldTip;

    def writePage(self):
        if self.getTip() is None:
            print('fail: nao existe grafite');
            return;

        if self.getTip().getSize() == 10:
            print('fail: tamanho insuficiente');
            return;

        if (self.getTip().getSize() - 10) < self.getTip().usagePerPage() and self.getTip().getSize() != 10:
            print('fail: folha incompleta');
            self.getTip().setSize(10);
            return;

        self.getTip().setSize(self.getTip().getSize() - self.getTip().usagePerPage());     
    # fim método do obejto