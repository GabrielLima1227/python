velocidade_do_carro = int(input("Qual a velocidade atual de seu carro? "))

if velocidade_do_carro > 80:
    multa = (velocidade_do_carro - 80) * 7
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km\h")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
print("Tenha um bom dia! Dirija com segurança!")