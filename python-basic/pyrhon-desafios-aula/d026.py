frase = input("Digite uma frase: ").lower().strip() 

print(f"Na sua frase a letra \"A\" aparece {frase.count("a")} vez/es")
print(f"A letra \"A\" aparece pela primeira vez na posição {frase.find("a")}")
print(f"A letra \"A\" aparece pela última vez na posição {frase.rfind("a")}")
