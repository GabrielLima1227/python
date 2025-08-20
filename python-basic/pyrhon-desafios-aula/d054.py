from datetime import date
maior_de_idade = 0 
menor_de_idade = 0

for i in range(1,8,1):
    ano_de_nascimento = int(input(f"Em que ano a {i}º pessoa nasceu? "))
    idade = date.today().year - ano_de_nascimento
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print(f"A todo temos {maior_de_idade} maiores de idade e {menor_de_idade} menores de idade.")