from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("""Suas Opções São:
[1]-Pedra
[2]-Papel
[3]-Tesoura""")
jogador = int(input("Qual a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("-="*10)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*10)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADO VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")