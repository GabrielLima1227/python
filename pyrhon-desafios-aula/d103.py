def ficha(jogador="", gols=0):
    return f"O jogador {jogador if jogador else '<desconhecido>'} fez {gols} gol(s) no campeonato."


nome_do_jogador = input("Nome do Jogador: ").strip()
numero_de_gols = input("Número de Gols: ").strip()

if numero_de_gols.isnumeric():
    numero_de_gols = int(numero_de_gols)
else:
    numero_de_gols = 0

print(ficha(nome_do_jogador, numero_de_gols))