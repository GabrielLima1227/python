nome_da_cidade = input("Digite o nome da sua cidade: ").strip()

print(f"A sua cidade começa com o nome Santo? {"santo" in nome_da_cidade[0: nome_da_cidade.find(" ")].lower()}")