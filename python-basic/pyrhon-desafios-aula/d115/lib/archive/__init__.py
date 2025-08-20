from d115.lib.interface import *


def arquivoExiste(nome):
    """
    Verifica se um arquivo existe no caminho especificado.
    Retorna True se existir, False caso contrário.
    """
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Cria um novo arquivo de texto.
    """
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    """
    Lê e exibe o conteúdo de um arquivo de texto.
    """
    try:
        with open(nome, "rt") as a:
            cabeçalho("PESSOAS CADASTRADAS")
            print(a.read())
    except FileNotFoundError:
        print(f"ERRO: O arquivo {nome} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
        return
    try:
        a.write(f"{nome};{idade}\n")
    except:
        print("Houve um ERRO na hora de escrever os dados!")
    else:
        print(f"Novo registro de {nome} adicionado.")

    a.close()
