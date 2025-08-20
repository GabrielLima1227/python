class Caneta:
    def __init__(self):
        self.modelo = ""
        self.cor = ""
        self.__ponta = 0
        self._carga = 0
        self._tampada = None

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Uma caneta {self.cor}")
        print(f"Ponta: {self.__ponta}")
        print(f"Carga: {self._carga}")
        print(f"Está Tampada? {self._tampada}")

    def __rabiscar(self):
        if self._tampada == False and self._carga > 50:
            print("rabiscando")
        else:
            print("Minha não caneta consegue rabiscar no momento.")

    def _tampar(self):
        if self.tampada == False:
            self.tampada = True

    def _destampar(self):
        if self.tampada == True:
            self.tampada = False


minha_caneta = Caneta()
minha_caneta.modelo = "Bic"
minha_caneta.cor = "Azul"
# minha_caneta.__ponta = 0.5
minha_caneta._Caneta__ponta = 0.5
minha_caneta._carga = 70
minha_caneta._tampada = False

minha_caneta.status()

# Isso dará erro!
minha_caneta.__rabiscar()
