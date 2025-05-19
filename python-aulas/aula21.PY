def fatorial(num=1):
    fat = 1
    for contador in range(num, 0, -1):
        fat *= contador
    return fat

valor = int(input("Digite um valor: "))
print(f"O fatorial de {valor} é {fatorial(valor)}")