nome_completo = input("Digite o seu nome completo: ").strip()

print(f"Seu nome com todas as letras em maiúsculo: {nome_completo.upper()}")
print(f"Seu nome com todas as letras em minusculo: {nome_completo.lower()}")

print(f"Qauntidade de letras do seu nome {len(nome_completo) - nome_completo.count(" ")}") #Opção 01
print(f"Qauntidade de letras do seu nome {len(nome_completo.replace(" ",""))}") #Opção 02

print(f"O seu primeiro nome tem {len(nome_completo[0: nome_completo.find(" ")])} letras") #Opção 01
primeiro_nome = nome_completo.split(" ")
print(f"O seu primeiro nome tem {len(primeiro_nome[0])} letras") #Opção 02  