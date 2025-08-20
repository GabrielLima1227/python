from modulo_d107 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {preco} e {moeda.metade(preco)}")
print(f"O dobro de {preco} é {moeda.dobro(preco)}")
print(f"Aumento de 10%, temos {moeda.aumentar(preco,10)}")
print(f"Reduzido em 13%, temos {moeda.diminuir(preco, 13)}")