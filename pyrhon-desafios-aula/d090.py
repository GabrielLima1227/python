boletim = {}
boletim['nome'] = str(input("Nome: ")).strip() 
boletim['media'] = float(input("Media: "))

print(f"\t - Nome é igual a {boletim['nome']}")
print(f"\t - Media é igual a {boletim['media']}")
if boletim['media'] >= 7:
    print(f"\t - Sitação é igual a Aprovado!")
elif boletim['media'] >= 5 and boletim['media'] < 7:
    print(f"\t - Sitação é igual a Recuperação!")
else:
    print(f"\t - Sitação é igual a Reprovado!")