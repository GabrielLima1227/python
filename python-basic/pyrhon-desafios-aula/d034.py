salario = float(input("Digite o valor de seu sálario: "))

if salario >= 1250:
    salario += salario * 0.10
    print(f"Você recebeu um almento de 10% no sálario agora seu sálario é R${salario}")
else:
    salario += salario * 0.15
    print(f"Você recebeu um almento de 15% no sálario agora seu sálario é R${salario}")