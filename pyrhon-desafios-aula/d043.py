peso = float(input("Quanto você pesa? (kg) "))
altura = float(input("Quanto você mede? (m) "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Você está ABAIXO DO PESO!")
elif 18 <= imc < 25:
    print("Você está no seu PESO IDEAL!")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO!")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está com OBESIDADE MÓRBIDA, cuidado!")
