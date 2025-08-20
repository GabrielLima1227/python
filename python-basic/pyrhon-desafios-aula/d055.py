maior_peso = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
    if pessoa == 1:
        maior_peso = menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso


print(f"O maior peso lido foi de {maior_peso}Kg")
print(f"O menor peso lido foi de {menor_peso}Kg")
