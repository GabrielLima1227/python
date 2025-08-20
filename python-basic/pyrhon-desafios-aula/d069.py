pessoas_com_18_ou_mais = usuarios_homens = mulheres_com_menos_de_vinte_anos = idade = sexo = prosseguir = 0

print("-" * 20)
print("CADASTRE UMA PESSOA")
print("-" * 20)

while idade == 0:
    idade = int(input("Digite a sua idade: "))
while sexo != "M" and sexo != "F":
    sexo = str(input("Qual o seu Sexo? [M/F] ")).upper().strip()[0]
if idade >= 18:
    pessoas_com_18_ou_mais += 1
if sexo == "M":
    usuarios_homens += 1
elif sexo == "F" and idade < 20:
    mulheres_com_menos_de_vinte_anos += 1

while True:
    idade = sexo = prosseguir = 0
    while prosseguir != "S" and prosseguir != "N":
        prosseguir = str(input("Deseja prosseguir cadastrando novas pessoas? [S/N] ")).upper().strip()[0]
        print("-" * 20)
    if prosseguir == "S":
            while idade == 0:
                idade = int(input("Digite a sua idade: "))
            while sexo != "M" and sexo != "F":
                sexo = str(input("Qual o seu Sexo? [M/F] ")).upper().strip()[0]
            if idade > 18:
                pessoas_com_18_ou_mais += 1
            if sexo == "M":
                usuarios_homens += 1
            elif sexo == "F" and idade < 20:
                mulheres_com_menos_de_vinte_anos += 1 
    elif prosseguir == "N":
        print("Encerrando o Programa")
        break
print(f"Total de pessoas com mais de 18 anos é {pessoas_com_18_ou_mais}")
print(f"Ao todo temos {usuarios_homens} homens cadastrados")
print(f"E temos {mulheres_com_menos_de_vinte_anos} com menos de 20 anos")