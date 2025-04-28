valor_casa = float(input("Qual o valor da casa que deseja comprar? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos deseja pagar o emprestimo? "))

prestacao = valor_casa / (anos * 12)

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a pretação será de R${prestacao:.2f}")
if prestacao < salario * 0.3:
    print(f"Empréstimo pode ser CONCEDIDO!")
else:
    print(f" Empréstimo NEGADO!")