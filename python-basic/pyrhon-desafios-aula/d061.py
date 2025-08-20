termo = int(input("Digite o termo da sua Progressão Aritmetica(PA): "))
razao = int(input("Digite a Razão de sua Progresão Aritmetica(PA): "))
progressao_aritmetica = termo
contador = 10
while contador > 0:
    print(progressao_aritmetica, end="->")
    progressao_aritmetica += razao
    contador -= 1
print("FIM!")