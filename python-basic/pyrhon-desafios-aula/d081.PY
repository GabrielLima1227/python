numeros = []
continuar = "S"

while True:
    numeros.append(int(input("Digite um valor: ")))
    while continuar == "S": 
        continuar = input("Deseja continuar? [S/N] ").upper().strip()[0]
        if continuar not in "SN":
            print("Opção inválida, tente novamente!")
            continuar = "S"
        elif continuar == "S":
            numeros.append(int(input("Digite um valor: ")))
    break
print("-="*20)
print(f"Você digitou {len(numeros)} elementos")
numeros.sort(reverse=True)
print(f"Os valores em ordem descrescente são {numeros}")
print(f"O valor 5 {"Faz parte da lista" if 5 in numeros else "Não faz parte da lista"}")