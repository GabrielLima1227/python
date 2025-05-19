def ler_inteiro(mensagem):
    numero_valido = False
    numero_inteiro = 0
    while True:
        entrada = input(mensagem)
        if entrada.isnumeric():
            numero_inteiro = int(entrada)
            numero_valido = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if numero_valido:
            break
    return numero_inteiro


# Programa principal
numero_digitado = ler_inteiro("Digite um número: ")
print(f"Você acabou de digitar o número {numero_digitado}")
