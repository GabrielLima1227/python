pessoas = {"nome": "Gabriel", "idade": 20, "sexo": "M"}

print(pessoas)
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos de idade")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for keys in pessoas.keys():
    print(keys)
for values in pessoas.values():
    print(values)
for items in pessoas.items():
    print(items)
for keys, values in pessoas.items():
    print(f"{keys} = {values}")

pessoas["peso"] = 66.0
for keys, values in pessoas.items():
    print(f"{keys} = {values}")

# Dicionários dentro de uma lista
brasil = []
estado01 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado02 = {"uf": "São Paulo", "sigla": "SP"}

brasil.append(estado01)
brasil.append(estado02)

print(estado01)
print(estado02)
print(brasil)

print(brasil[0])
print(brasil[0]["uf"])
print(brasil[0]["sigla"])

print(brasil[1])
print(brasil[1]["uf"])
print(brasil[1]["sigla"])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
