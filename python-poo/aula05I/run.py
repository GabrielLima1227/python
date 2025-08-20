# Variáveis de Classe
class MinhaClasse:
    estatico = "Gabriel"

    def __init__(self,estado) -> None:
        self.estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "Lima"
obj1.estado = "Sousa"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
