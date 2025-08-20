lanches = ("Hambúrguer", "Coxinha", "Pizza", "Pudim")
#Tuplas são Imutáveis
#lanches[1] = "Coca-Cola" Isso não é válido
print(lanches)
print(lanches[1])
print(lanches[-2])
print(lanches[1:3])
print(lanches[2:])
print(lanches[:2])
print(lanches[0::2])
print(lanches[-2:])
print(lanches[-3::2])
print(lanches[-3::-1])
print("-="*20)
print(len(lanches))
print("-="*20)
for Lanche in lanches:
    print(Lanche)
print("-="*20)
for Contador in range (0, len(lanches)):
    print(lanches[Contador])
print("-="*20)
print(sorted(lanches))
print("-="*20)
bebidas = ("Suco","Coca-Coal","Fanta","Guaranáx")
Merenda = lanches + bebidas
print(Merenda)
