numero = int(input("Digite um número: "))
fatoreal = contador = numero

while contador > 1:
    fatoreal *= (contador -1)
    contador -= 1
print(f"O fatoreal de {numero} é igual a {fatoreal}")