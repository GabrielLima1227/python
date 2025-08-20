from math import sin, cos, tan, radians
angulo = float(input("Digite o valor de um angulo: "))

print(f"O seno do angulo {angulo}º é {sin(radians(angulo)):.2f}")
print(f"O cosseno do angulo {angulo}º é {cos(radians(angulo)):.2f}")
print(f"A tangente do angulo {angulo}º é {tan(radians(angulo)):.2f}")