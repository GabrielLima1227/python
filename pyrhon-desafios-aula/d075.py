
numeros = (int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")), int(input("Digite o terceiro valor: ")), int(input("Digite o quarto valor: ")), int(input("Digite o quinto valor: ")))

pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(f"Você digitou os valores {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3) + 1}º posição")
print(f"Os valores pares digitados foram {pares}")