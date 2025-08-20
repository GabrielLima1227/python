class Caneta:
    def __init__(self):
        self.modelo = ""
        self.cor = ""
        self.ponta = 0
        self.carga = 0
        self.tampada = None
    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Uma caneta {self.cor}")
        print(f"Ponta: {self.ponta}") 
        print(f"Carga: {self.carga}")
        print(f"Está Tampada? {self.tampada}")
    def rabiscar(self):
        if self.tampada == False and self.carga > 50:
            print("rabiscando")
        else:
            print("Minha não caneta consegue rabiscar no momento.")
    def tampar(self):
        if self.tampada == False:
            self.tampada = True
    def destampar(self):
        if self.tampada == True:
            self.tampada = False

minha_caneta = Caneta()
minha_caneta.modelo = "Bic"
minha_caneta.cor = "Azul"
minha_caneta.ponta = 0.5
minha_caneta.carga = 70
minha_caneta.tampada = False

minha_caneta.status()
minha_caneta.rabiscar()