from random import randint
from time import sleep

jogadores_numreos_da_sorte = {}

print("Valores Sorteados:")
for posicao in range(1, 5):
    jogadores_numreos_da_sorte[f'jogador{posicao}'] = randint(1, 6)
    print(f'O jogador{posicao} tirou {jogadores_numreos_da_sorte[f"jogador{posicao}"]}')
    sleep(1)

# Ordenar pelos valores sorteados (em ordem crescente) 
jogadores_numreos_da_sorte = dict(sorted(jogadores_numreos_da_sorte.items(), key=lambda item: item[1], reverse=True))

print("\nRanking dos Jogadores:")
for idx, (jogador, valor) in enumerate(jogadores_numreos_da_sorte.items(), start=1):
    print(f'{idx}º Lugar: {jogador} com {valor}')
