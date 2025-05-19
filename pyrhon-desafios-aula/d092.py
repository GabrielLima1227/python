from datetime import date

aposentadoria = {}

aposentadoria['nome'] = str(input("Nome: ")).strip()
aposentadoria['idade'] = date.today().year  - int(input("Ano de Nascimento: "))
aposentadoria['carteira_de_trabalho'] = int(input("Carteira de trabalho (0 não tem): "))
if aposentadoria['carteira_de_trabalho'] > 0:
    aposentadoria['ano_de_contrato'] = int((input("Ano de Contratação: ")))
    aposentadoria['salario'] = float(input("Sálario: R$"))
    aposentadoria['aposento'] = 35 - (date.today().year - aposentadoria['ano_de_contrato']) + aposentadoria['idade']

print("-="*30)
for chave,valor in aposentadoria.items():
    print(f"{chave} tem o valor {valor}")