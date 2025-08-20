soma_pares = 0
for i in range(1,7,1):
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        soma_pares += numero
print(f"A soma dos números pares que você digitou é {soma_pares}")
