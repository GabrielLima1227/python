nome_completo = input("Digite seu nome completo: ").strip()

print(f"Primeiro nome {nome_completo[0: nome_completo.find(" ")]}")

ultimo_nome = nome_completo.split(" ")
print(f"Último nome {ultimo_nome[-1]}")