from random import randint
from time import sleep


def sortear_valores(lista_numeros):
    print("Sorteando 5 valores da lista:", end=" ")
    for _ in range(5):
        numero_sorteado = randint(1, 10)
        lista_numeros.append(numero_sorteado)
        print(f"{numero_sorteado}", end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")


def somar_pares(lista_numeros):
    soma_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
    print(f"Somando os valores pares de {lista_numeros}, temos {soma_pares}")


# Programa principal
lista_de_numeros = []
sortear_valores(lista_de_numeros)
somar_pares(lista_de_numeros)
