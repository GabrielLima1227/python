termo = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Qual é a razão da sua PA? "))
decimo_termo = termo + (10 -1) * razao
for i in range(termo,decimo_termo + razao, razao):
    print(f"{i}", end="->")
print("Acabou")
