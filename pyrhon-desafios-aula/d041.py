from datetime import date
ano_de_nascimeto = int(input("Qual o seu ano de nascimento? "))

idade = date.today().year - ano_de_nascimeto

print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Classificaçõa: Mirim")
elif idade <= 14:
    print("Classificaçõa: Infantil")
elif idade <= 19:
    print("Classificaçõa: Junior")
elif idade <= 20:
    print("Classificaçõa: Sênior")
else:
    print("Classificaçõa: Master")
