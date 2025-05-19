from datetime import date


def voto(ano_de_nascimento):
    idade = date.today().year - ano_de_nascimento
    if idade < 16:
        return idade, "VOTO NEGADO"
    elif idade >= 16 and idade < 65:
        return idade, "VOTO OBRIGATÓRIO"
    elif idade >= 65:
        return idade, "VOTO OPICIONAL"


data_de_nascimento = int(input("Em que ano você nasceu? "))
idade, status = voto(data_de_nascimento)
print(f"Com {idade} anos: {status}") 