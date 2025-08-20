class Caneta:
    def __init__(self, *args) -> None:
        self.modelo = ""
        self.cor = "Azul"
        self.__ponta = 0.0
        self.setter_ponta(args[2])
        self.__tampada = None
        self.tampar()

    def status(self) -> None:
        print("Sobre a Caneta")
        print(f"Modelo: {self.modelo}")
        print(f"Ponta: {self.__ponta}")
        print(f"Cor: {self.cor}")
        print(f"Tampada: {self.__tampada}")

    def getter_modelo(self) -> str:
        return self.modelo
    def setter_modelo(self, nome: str) -> None:
        self.modelo = nome

    def getter_ponta(self) -> float:
        return self.__ponta    
    def setter_ponta(self, valor: float) -> None:
        self.__ponta = valor

    def tampar(self) -> None:
        self.__tampada = True

    def destampar(self) -> None:
        self.__tampada = False

caneta_azul = Caneta("Bic Cristal","Azul",0.7)

print()
caneta_azul.status()