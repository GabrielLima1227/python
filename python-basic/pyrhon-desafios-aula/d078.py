numeros = []
contador = 0
posicao_maior_valor = []
posicao_menor_valor = []

for valores in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {valores}: ")))

for indice, valor in enumerate(numeros):
    if valor == max(numeros):
        posicao_maior_valor.append(indice)
    if valor == min(numeros):
        posicao_menor_valor.append(indice)

print(f"O maior valor digitado foi {max(numeros)} e sua(s) posição(ões) na lista é(são) {posicao_maior_valor}")
print(f"O menor valor digitado foi {min(numeros)} e sua(s) posição(ões) na lista é(são) {posicao_menor_valor}")
