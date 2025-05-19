def notas(*valores, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.
    Parâmetros
    ----------
    *valores : tuple
        Uma ou mais notas dos alunos (pode receber múltiplos valores).
    situacao : bool, opcional
        Indica se deve ou não incluir a situação da turma com base na média. Por padrão, é False.
    Retorna
    -------
    dict
        Um dicionário contendo informações sobre a quantidade de notas, maior nota, menor nota,
        média da turma e, opcionalmente, a situação (como 'Boa', 'Razoável' ou 'Ruim').
    """
    ficha = {}
    ficha["total"] = len(valores)
    ficha["maior_nota"] = max(valores)
    ficha["menor_nota"] = min(valores)
    ficha["media"] = sum(valores) / len(valores)
    if situacao == True:
        if ficha["media"] >= 7:
            ficha["situacao"] = "BOA"
        elif 5 <= ficha["media"] < 7:
            ficha["situacao"] = "RAZOÁVEL"
        else:
            ficha["situacao"] = "RUIM"
    return ficha


resposta = notas(9, 8, 4, situacao=True)
print(resposta)
help(notas)
