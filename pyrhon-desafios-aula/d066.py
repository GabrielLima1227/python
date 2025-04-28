numero = soma = quantidade = 0
while True:
    numero = int(input("Digite um número [999 Para Encerrar a Execução]: "))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f"A soma dos {quantidade} valores é {soma}!")