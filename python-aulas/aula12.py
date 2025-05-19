nome = str(input("Qual e o seu nome? "))

if nome == "Gabriel":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria":
    print("Seu nome é popular no Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome Feminino")
else:
    print("Seu nome é bem normal.")

print(f"Tenha um bom dia, {nome}!")