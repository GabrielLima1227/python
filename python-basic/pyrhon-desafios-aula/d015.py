dias_de_aluguel = int(input("Quantos dias o carro foi alugado? "))
km_rodados = float(input("Qauntos Km foram rodados? "))
preco_total = (dias_de_aluguel * 60) + (km_rodados * 0.15)

print(f"O total a pagar é de R${preco_total:.2f}") 