def soma(parcela01,parcela02):
    total = parcela01 + parcela02
    print(f"A soma de {parcela01} mais {parcela02} é igual a {total}")

soma(4,5)

#Tupla como parâmetro
def contador(*numero):
    for valor in numero:
        print(valor)


contador(1,2,3,4,5,6,7,)
contador(1,2,3)

#Lista como parâmetro
valores = [1,2,3,4,5]

def dobra_valores(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
        

dobra_valores(valores)
print(valores)