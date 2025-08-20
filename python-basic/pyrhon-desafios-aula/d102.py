def fatorial(numero, show=False):
    """
    fatorial(numero, show=False)
    -> Calcula o Fatorial de um Número
    Parameters
    ----------
    numero : _type_
        O número a Ser Calculado o Fatortial.
    show : bool, optional
        Mostra ou Não o Processo da Conta, Por Padrão False
    """
    fatorial_de_um_numero = 1
    print("-" * 30)
    if show == True:
        for contador in range(numero, 0, -1):
            fatorial_de_um_numero *= contador
            print(f"{contador} {"x" if contador > 1 else "="}", end=" ")
    else:
        for contador in range(numero, 0, -1):
            fatorial_de_um_numero *= contador
    return fatorial_de_um_numero

print(fatorial(5, True))
print(fatorial(5))