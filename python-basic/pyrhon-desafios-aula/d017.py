from math import hypot
cateto_oposto = float(input("Digite o valor do cateto oposo: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(f"O triângulo retângulo com cateto oposto de {cateto_oposto} e cateto adjacente de {cateto_adjacente} tem hipotenusa de {hipotenusa:.2f}")