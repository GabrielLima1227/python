from random import randint
numeros_aleartorios = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100))

print(numeros_aleartorios)
print(max(numeros_aleartorios))
print(min(numeros_aleartorios))

print("-=" * 20) #ou

print(sorted(numeros_aleartorios)[-1])
print(sorted(numeros_aleartorios)[0])