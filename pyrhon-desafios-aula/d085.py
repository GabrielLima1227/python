lista_par_impar = [[],[]]
for contador in range (0,7):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        lista_par_impar[0].append(valor)
    else:
        lista_par_impar[1].append(valor)
print("-="*30)
lista_par_impar[0].sort()
lista_par_impar[1].sort()
print(f"O valores pares digitados foram: {lista_par_impar[0]}")
print(f"O valores impares digitados foram: {lista_par_impar[1]}")