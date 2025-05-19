"""""for i in range(1,10):
        print(i)
print("FIM!")
"""

"""i = 1
while i < 10:
    print(i)
    i += 1
print("FIM")"""

numero = 1
par, impar = 0, 0
while numero != 0:
    numero = int(input("Digite um valor inteiro: "))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} números pares e {impar} números impares!")