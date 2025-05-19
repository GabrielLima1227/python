from random import randint
from time import sleep

lista_de_jogos = []

print("-"*30)
print("JOGA NA MEGA SENA")
print("-"*30)

numeros_de_jogos = int(input("Quantos jogos você quer que eu sorteie? "))

print(f"-=-=-= SORTEANDO {numeros_de_jogos} JOGOS -=-=-=")
for contador in range(0,numeros_de_jogos):
    lista_de_jogos.append([])
    for numero_da_sorte in range(0,5):
        lista_de_jogos[contador].append(randint(1,60))
    print(f"Jogo {contador + 1}: {lista_de_jogos[contador]}")
    sleep(1)
print("-=-=-= < BOA SORTE! > -=-=-=")
