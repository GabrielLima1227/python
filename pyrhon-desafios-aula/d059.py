valores = []
valores.append(float(input("Digite o seu primeiro valor: ")))
valores.append(float(input("Digite o seu segundo valor: ")))
operacao = 0
opcao = 0
while opcao != 5:
    opcao = int(
    input(
        """ Qual operações você deseja realizar com os números?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Nnúmeros
    [5] Sair do Programa
    """
    )
    )
    if opcao == 1:
        operacao = sum(valores)
        print(f"A soma dos voleres é igual a {operacao}")
    elif opcao == 2:
        operacao = 1
        for valor in valores:
            operacao *= valor
        print(f"A multiplicação dos valores é igual a {operacao}")
    elif opcao == 3:    
        operacao = max(valores)
        print(f"O maior número dentre os valores digitados é {operacao}")
    elif opcao == 4:
        valores.append(float(input("Digite um valor adicional: ")))
    elif opcao == 5: 
        print("O progama está se encerrando")
    else:
        print("Digite uma opção válida")
print("Fim do Programa! Volte Sempre!")