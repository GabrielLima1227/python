numero = int(input("Digite o primeiro termo da sua sequência de Fibonacci: "))
repeticao = int(input("Quantas vezes a sequência deve se repetir? "))
numero_anteriro = 0

while repeticao >= 0:
    print(numero + numero_anteriro, end="->")
    numero = numero_anteriro + numero
    numero_anteriro = numero - numero_anteriro
    repeticao -= 1
print("Fim")