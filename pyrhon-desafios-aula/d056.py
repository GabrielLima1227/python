soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
total_mulheres_menos_20 = 0

for pessoa in range(1, 5):
    print(f"----- {pessoa}ª PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idade += idade

    if sexo == "M":
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    elif sexo == "F" and idade < 20:
        total_mulheres_menos_20 += 1

media_idade = soma_idade / 4

print(f"\nA média de idade do grupo é de {media_idade:.1f} anos.")
if nome_homem_mais_velho:
    print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.")
else:
    print("Não há homens no grupo.")
print(f"Ao todo, são {total_mulheres_menos_20} mulher(es) com menos de 20 anos.")
