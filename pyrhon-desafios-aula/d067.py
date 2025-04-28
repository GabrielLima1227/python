contador = valor = 1 
while True:
    print("-" * 15)
    valor = int(input("Quer ver a Tabuada de qual valor? "))
    print("-" * 15)
    if valor >= 0:
        contador = 1
        for contador in range(1,11):
            print(f"{valor} x {contador} = {valor*contador}")
            contador += 1
    else:
        print(f"PROGRAMA DE TABUADA ENCERRADO. Volte Sempre!")
        break