distancia_da_viagem = float(input("Digite qual a distância da viagem: "))

if distancia_da_viagem <= 200:
    print(f"Você está prestes a começar um viagem de {distancia_da_viagem:.1f}Km")
    print(f"O valor da sua passagem é de R${distancia_da_viagem * 0.50}")
else:
    print(f"Você está prestes a começar um viagem de {distancia_da_viagem:.1f}Km")
    print(f"O valor da passagem é de {distancia_da_viagem * 0.45}")

