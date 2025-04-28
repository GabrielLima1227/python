somatorio = 0
for i in range(1, 501,1):
    if i % 3 == 0:
        if i % 2 == 1:
            somatorio += i
print(f"O somatorio de todos os números impares e multiplos de 3 entre 1 e 500 é {somatorio}")

# Ou 
somatorio = 0
for i in range(3, 501, 3):
    if i % 2 == 1:
        somatorio += i
print(f"O somatorio de todos os números impares e multiplos de 3 entre 1 e 500 é {somatorio}")  

# Ou
somatorio = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        somatorio += i
print(f"O somatorio de todos os números impares e multiplos de 3 entre 1 e 500 é {somatorio}")  
