from modulo_d109 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} e {moeda.metade(preco,False)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco,True)}")
print(f"Aumento de 10%, temos {moeda.aumentar(preco,10,True)}")
print(f"Reduzido 13%, temos {moeda.diminuir(preco,13,True)}")