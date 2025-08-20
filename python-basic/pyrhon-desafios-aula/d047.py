print("Esses são todos os números pares entre 1 e 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i}")

# Ou pode ser assim também
print("Esses são todos os números pares entre 1 e 50")
for i in range(2, 51, 2):
    print(i)
