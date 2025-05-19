numeros = []

for valores in range(0, 5):
    valor = int(input("Digite um valor: "))
    
    if valor not in numeros:
        inserted = False
        for contador in range(len(numeros)):
            if valor > numeros[contador] and (contador + 1 < len(numeros) and valor < numeros[contador + 1]):
                numeros.insert(contador + 1, valor)
                inserted = True
                break
        if not inserted:
            numeros.append(valor)
print(numeros)