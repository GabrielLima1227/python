from time import sleep
def linha():
    print("-=" * 30)

def contador(inicio, fim, passo):
    linha()
    print(f"Contagem de {inicio} até {fim} a um passo de {passo} em {passo}")
    if inicio < fim:
        if passo > 0:
            while inicio < fim:
                print(inicio, end=" ", flush=True)
                inicio += passo
                sleep(0.2)
            print("FIM!")
        elif passo == 0:
            while inicio <= fim:
                print(inicio, end=" ", flush=True)
                inicio += 1 
                sleep(0.2)
            print("FIM!")
        else:
            print("Passo inválido para contagem crescente!")
    if inicio > fim:
        if passo > 0:
            while fim <= inicio:
                print(inicio, end=" ", flush=True)
                inicio -= passo
                sleep(0.2)
            print("FIM!")
        elif passo == 0:
            while fim <= inicio:
                print(inicio, end=" ", flush=True)
                inicio -= 1
                sleep(0.2)
            print("FIM!")
        else:
            while fim <= inicio:
                print(inicio, end=" ", flush=True)
                inicio += passo
                sleep(0.2)
            print("FIM!")


contador(1, 10, 1)
contador(10, 0, -2)

linha()
print("Agora e a sua vez de personalizar a contagem!")
ponto_inicial = int(input("Início: "))
ponto_final = int(input("Final: "))
passo = int(input("Passo da contagem: "))

contador(ponto_inicial, ponto_final, passo)
