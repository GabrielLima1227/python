def aumentar(valor=0, porcentagem=0,format=False,moeda="R$"):
    if format:
        return f"{moeda}{valor + ((valor * porcentagem)/ 100)}".replace(".", ",")
    return valor + ((valor * porcentagem) / 100)


def diminuir(valor=0, porcentagem=0,format=False,moeda="R$"):
    if format:
        return f"{moeda}{valor - ((valor * porcentagem)/ 100)}".replace(".", ",")
    return valor - ((valor * porcentagem) / 100)


def dobro(valor=0,format=False,moeda="R$"):
    if format:
        return f"{moeda}{valor * 2}".replace(".", ",")
    return valor * 2


def metade(valor=0,format=False,moeda="R$"):
    if format:
        return f"{moeda}{valor/2}".replace(".", ",")
    return valor / 2


def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")

def resumo(valor,acrescimo, reducao):
    print("-=" * 20)
    print(f"{'RESUMO DO VALOR':>5}")
    print("-=" * 20)
    print(f"{'Preço analisado:':<25} R${valor:.2f}")
    print(f"{'Dobro do Preço:':<25} {dobro(valor,True)}")
    print(f"{'Metade do Preço:':<25} {metade(valor,True)}")
    print(f"{acrescimo}% {'de Aumento:':<21} {aumentar(valor,acrescimo,True)}")
    print(f"{reducao}% {'de Aumento:':<21} {diminuir(valor,reducao,True)}")
    print("-=" * 20)