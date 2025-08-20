lista_pessoa_e_peso = []
lista_composta_pessoa_peso = []
maior_peso = menor_peso = 0

while True:
    nome = input("Nome: ").strip()
    peso = int(input("Peso: "))
    lista_pessoa_e_peso.append([nome, peso])
    if len(lista_pessoa_e_peso) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

print("-=" * 30)
print(f"Ao todo, você cadastrou {len(lista_pessoa_e_peso)} pessoas.")
print(f"O maior peso foi {maior_peso}kg. Peso de ", end="")
for pessoa in lista_pessoa_e_peso:
    if pessoa[1] == maior_peso:
        print(f"[{pessoa[0]}] ", end="")
print()

print(f"O menor peso foi {menor_peso}kg. Peso de ", end="")
for pessoa in lista_pessoa_e_peso:
    if pessoa[1] == menor_peso:
        print(f"[{pessoa[0]}] ", end="")
print()