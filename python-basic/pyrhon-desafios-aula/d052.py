numero = int(input("Digite um número: "))
primo = True
for i in range(2,numero):
    if primo:
        if numero == 2:
            primo = True
        elif numero % i == 0:
            primo = False

print(f"O seu número {"é primo" if primo else "não é primo"}")
