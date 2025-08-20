resposta = "S"
#soma, quantidade, media, maior, menor = 0,0,0,0,0
soma = quantidade = media = maior = menor = 0
while resposta == "S":
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    resposta = input("Deseja continuar [S/N]? ").upper().strip()[0]
media = soma / quantidade
print(f"Você digitou {quantidade} e a média foi {media}")
print(f"O maior valor digitado foi {maior} e o menor {menor}")
