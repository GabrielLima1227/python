pessoas = []
pessoa = {}
continuar = "S"
soma_das_idades = 0

while True:
    pessoa['nome'] = str(input("Nome: ")).strip()
    pessoa['idade'] = int(input("Idade: "))
    soma_das_idades += pessoa['idade']
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while continuar == "S":
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar not in "SN":
            print("Por Favor Digite um Opção Válida, Tente Novamente!")
            continuar = "S"
        elif continuar == "S":
                pessoa['nome'] = str(input("Nome: ")).strip()
                pessoa['idade'] = int(input("Idade: "))
                soma_das_idades += pessoa['idade']
                pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
                pessoas.append(pessoa.copy())
                pessoa.clear()
        elif continuar == "N":
            print("Encerrando Progama.")
        
    break

print(pessoas)
print("-=" * 30)
print(f"\t - O grupo tem {len(pessoas)} pessoas.")
print(f"\t - A média de idade é de {soma_das_idades / len(pessoas)} anos.")

print(f"\t - As Mulheres cadastradas foram: ", end='')
for contador in range(0,len(pessoas)):
    if pessoas[contador]['sexo'] == "F":
        print(pessoas[contador]['nome'], end=',')
print()
print(f"\t - Lista das pessoas que estão acima da média: ")
for contador in range(0,len(pessoas)):
    if pessoas[contador]['idade'] > soma_das_idades / len(pessoas):
        print(f"\t {pessoas[contador]};")
print("\t << ENCERRADO >>")