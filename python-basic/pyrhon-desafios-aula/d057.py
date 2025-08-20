sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0]
while sexo != "M" and sexo != "F":
    sexo = input("Dados Inválidos. Por favor, informe o seu sexo [M/F]: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")