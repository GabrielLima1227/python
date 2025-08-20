# Getters/Setters e Encapsulamentos
class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None
        """
        def setter(self, valor: int) -> None:
        self.__valor = valor
    def getter(self) -> int:
        return self.__valor
        """

    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    def getter_valor(self) -> int:
        return self.__valor


my_class = MinhaClasse()

# my_class.setter(42)
# valor = my_class.getter()

my_class.setter_valor(42)
valor = my_class.getter_valor()

print(valor)
