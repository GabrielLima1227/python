numero = int(input("Digite um número: "))

print(f"A tabuada do número {numero} é")
print("-"*12)
for i in range(1, 11, 1):
    print(f"{numero} x {i} = {numero*i}")
print("-"*12)