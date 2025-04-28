numero = input("Digite um número entre 0 e 9999: ").strip()

# Esse método dará erro caso o usuário digite um número com menos de 4 algarismos.
#Opção 01
#print(f"Unidades: {numero[3]}")
#print(f"Dezenas: {numero[2]}")
#print(f"Centenas: {numero[1]}")
#print(f"Milhar: {numero[0]}")

#Opção 02
numero = int(numero)
unidades = numero // 1 % 10
dezenas = numero // 10 % 10
centenas = numero // 100 % 10
milhares = numero // 1000 % 10

print(f"Unidades: {unidades}")
print(f"Dezenas: {dezenas}")
print(f"Centenas: {centenas}")
print(f"Milhar: {milhares}")