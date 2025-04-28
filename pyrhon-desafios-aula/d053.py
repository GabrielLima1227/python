frase = input("Escreva um palavra ou farse qualquer: ").strip()
palindromo = "".join(frase.lower().split(" "))

if palindromo == palindromo[::-1]: 
    print("A frase é um palindromo")
else:
    print("A frase não é um palindromo")
