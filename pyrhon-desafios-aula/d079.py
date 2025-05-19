numeros = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in numeros:
        print("Valor duplicado! Não vou adicionar...")
    else:
        numeros.append(valor)
        print("Valor adcionado com sucesso...")
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break
print("-=" * 20)
numeros.sort()  
print(f"Você digitou os valores: {numeros}")
