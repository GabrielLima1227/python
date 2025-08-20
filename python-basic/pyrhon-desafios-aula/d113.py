def leia_inteiro(mensagem_prompt):
    """
    Lê um número inteiro do usuário, tratando erros de entrada.
    Retorna 0 se o usuário interromper a entrada.
    """
    while True:
        try:
            valor_lido = int(input(mensagem_prompt))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_lido


def leia_real(mensagem_prompt):
    """
    Lê um número real (float) do usuário, tratando erros de entrada.
    Retorna 0 se o usuário interromper a entrada.
    """
    while True:
        try:
            valor_lido = float(input(mensagem_prompt))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_lido


numero_inteiro_digitado = leia_inteiro("Digite um Inteiro: ")
numero_real_digitado = leia_real("Digite um Real: ")

print(f"O valor inteiro digitado foi {numero_inteiro_digitado} e o real foi {numero_real_digitado}")
