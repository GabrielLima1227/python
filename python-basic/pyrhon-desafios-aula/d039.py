from datetime import date
ano_de_nascimeto = int(input("Qual o seu ano de nascimento? "))

idade = date.today().year - ano_de_nascimeto

print(f"Quem nasceu em {ano_de_nascimeto} tem {idade} anos em {date.today().year}")
if idade < 18:
    tempo_ate_o_alistamento = 18 - idade
    print(f"Ainda faltam {tempo_ate_o_alistamento} anos para o alistamento")
    print(f"Seu alistamento será em {ano_de_nascimeto + 18}")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
else:
    tempo_passo_do_alistamento = idade - 18
    print(f"Você já deveria ter se alistado há {tempo_passo_do_alistamento} anos.")
    print(f"Seu alistamento foi em {ano_de_nascimeto + 18}")