aproveitamento = {}
gols = []

aproveitamento['nome'] = str(input("Nome: ")).strip()
aproveitamento['partidas'] = int(input(f"Quantas partidas {aproveitamento['nome']} jogou? "))

for contador in range(0,aproveitamento['partidas']):
    gols.append(int(input(f"Quantos gols {aproveitamento['nome']} fez na partida {contador}? ")))   
aproveitamento['gols'] = gols
aproveitamento['total_de_gols'] = sum(gols)

print("-=" * 30)
print(aproveitamento)
print("-=" * 30)
for chave, valor in aproveitamento.items():
    print(f"O campo {chave} tem valor de {valor}.")

print("-=" * 30)
print(f"O jogador {aproveitamento['nome']} jogou {aproveitamento['partidas']} partidas.")
for contador in range(0,aproveitamento['partidas']):
    print(f"\t => Na partida {contador}, fez {aproveitamento['gols'][contador]} gols")
print(f"Foi um total de {aproveitamento['total_de_gols']} gols")