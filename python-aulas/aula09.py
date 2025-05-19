frase = " Curso em Video Python "

print(frase[9])
print(frase[9:14])
print(frase[9:14:2])
print(frase[:14])
print(frase[9:])
print(frase[9::2])  

print(len(frase))
print(frase.count("o"))
print(frase.count("o",9,))
print(frase.find("Video"))
print(frase.find("V",0,7))
print("Video" in frase)

print(frase.replace("Curso", "Faculdade"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())


dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3])

Junto = " ".join(dividido[0:4])
print(Junto)