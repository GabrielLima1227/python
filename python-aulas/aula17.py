numeros = [2,5,9,1]
numeros[2] = 3
print(numeros)

numeros.append(7)
print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros.insert(0, 8)
print(numeros)

print(f"Essa lista tem {len(numeros)} números")

del numeros[0]
print(numeros)

numeros.pop()
print(numeros)

numeros.remove(7)
print(numeros)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate (valores):
    print(f'Na posição {c} encentrei o valor {v}!')
print('Cheguei ao final da lista.')