from random import random
from math import trunc

numero = trunc(random() * 6)

print("-=" * 10)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=" * 10)

seu_chute = int(input("Em que número eu pensei? "))

if seu_chute == numero:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print(f"Ganhei,Eu pensei no número {numero} e não no {seu_chute}!")

