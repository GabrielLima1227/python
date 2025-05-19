#import math
import random
from math import sqrt, floor
numero = int(input("Digite um número: "))
#raiz = math.sqrt(numero)
raiz = sqrt(numero)
#print(f"A raiz de {numero} é {raiz:.2f}")
print(f"A raiz de {numero} é {floor(raiz)}")

numero_random = random.random()
print(f"{numero_random}")
numero_random = random.randint(1, numero)
print(f"{numero_random}")

