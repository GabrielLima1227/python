nome_do_produto = nome_do_produto_mais_barato = ""
preco = total = mais_de_mil = menor_preco = contador = 0

while True:
    nome_do_produto = str(input("Nome do produto: "))
    preco = float(input("Preço do Produto: R$"))
    contador += 1
    total += preco
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        nome_do_produto_mais_barato = nome_do_produto
    resposta = ""
    if preco > 1000:
        mais_de_mil += 1
    while resposta not in ("S", "N"):
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resposta == "N":
        break

print("FIM DO PROGRAMA")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {mais_de_mil} produtos custando acima de R$1000.00")
print(f"O produto mais barato foi {nome_do_produto_mais_barato} que custa R${menor_preco:.2f}")
