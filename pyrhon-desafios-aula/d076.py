produtos = ("Arroz", 5.99, "Feijão", 6.49, "Macarrão", 3.79, "Leite", 4.25, "Café", 9.89)

print("-"*20)
print("LISTAGEM DE PREÇOS")
print("-"*20)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome} {'.' * (20 - len(nome))} R${preco:.2f}")
print("-"*20)