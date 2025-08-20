# Visibilidade em Python
class Pessoa:
    def __init__ (self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f"Ola! Minha altura {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f"Meu documento - {self.__cpf}")

jorge = Pessoa("1.70", "123-456-789-00")

jorge.__cpf = "123abc"
print(jorge.__cpf)

jorge.apresentar()