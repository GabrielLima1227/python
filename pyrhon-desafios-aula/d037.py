numero = int(input("Digite um número: "))
print(""" Escolha uma base de conversão:
[01]-Binario
[02]-Octal
[03]-Hexadecial
""")

opcao_de_conversao = int(input("Sua opção: "))



if opcao_de_conversao == 1:
    print(f"{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}")
elif opcao_de_conversao == 2:
    print(f"{numero} convertido para OCTAL é igual a {oct(numero)[2:]}")
elif opcao_de_conversao == 3:
    print(f"{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}")
else:
    print("Escolha uma opção de conversão Válida")
