primeiro_numro = int(input("Digite o primeiro número da comparação: "))
segundo_numero = int(input("Digite o segundo número da comparação: "))

if primeiro_numro > segundo_numero:
    print(f"O primeiro valor é MAIOR")
elif segundo_numero > primeiro_numro:
    print(f"O Segundo valor é MAIOR")
else:
    print(f"Os números são iguais")
