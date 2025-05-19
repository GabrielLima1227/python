numeros, sublista_par, sublista_impar = [], [], []
continuar = "S"

while True:
    valor = int(input("Digite um valor: "))
    while continuar == "S":
        numeros.append(valor)
        if valor in numeros:
            print("O valor já foi digitado, tente novamente")
        elif valor % 2 == 0:
            sublista_par.append(valor)
        else:
            sublista_impar.append(valor)
        continuar = str(input("Deseja Continuar? [S/N] ")).strip().upper()[0]
        if continuar not in "SN":
            print("Opção inválida, tente novamente!")
            continuar = "S"
        elif continuar == "S":
            valor = int(input("Digite um valor: "))
    break
print("-=" * 20)
print(f"A lista completa é {numeros}")
print(f"A lista de pares é {sublista_par}")
print(f"A lista de ímpares é {sublista_impar}")
