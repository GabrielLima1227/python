matriz = [[],[],[]]
soma_valores_pares = soma_terceira_coluna = maior_valor_segunda_linha = 0

for indice in range(0,3):
    matriz[indice].append(int(input(f"Digite um valor para [{indice},0]: ")))
    matriz[indice].append(int(input(f"Digite um valor para [{indice},1]: ")))
    matriz[indice].append(int(input(f"Digite um valor para [{indice},2]: ")))
    for subindice in range(0,3):
        if matriz[indice][subindice] % 2 == 0:
            soma_valores_pares += matriz[indice][subindice]
        if matriz[indice][subindice] == matriz[indice][2]:
            soma_terceira_coluna += matriz[indice][2]
        if indice == 1:
            if matriz[indice][subindice] == matriz[1][subindice] and matriz[indice][subindice] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[indice][subindice]

print("-=" * 30)
print(f"[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]")
print(f"[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]")
print(f"[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]")
print("-=" * 30)
print(f"A soma dos valores pares é {soma_valores_pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é {maior_valor_segunda_linha}")