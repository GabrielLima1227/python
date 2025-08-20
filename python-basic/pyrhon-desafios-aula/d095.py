# Listas e dicionários principais
time = list()
jogador = dict()
partidas = list()

# Loop principal
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    partidas.clear()
    for partida in range(total_partidas):
        gols = int(input(f'Quantos gols na partida {partida + 1}? '))
        partidas.append(gols)

    jogador['gols'] = partidas[:]  # cópia da lista
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

# Exibição do resumo
print('-' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
print('-' * 40)

for indice, jogador in enumerate(time):
    print(f'{indice:<4}', end='')
    print(f'{jogador["nome"]:<15}', end='')
    print(f'{str(jogador["gols"]):<20}', end='')
    print(f'{jogador["total"]:<5}')
print('-' * 40)

# Detalhes de cada jogador
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca < 0 or busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for partida, gols in enumerate(time[busca]['gols']):
            print(f'  No jogo {partida + 1} fez {gols} gols.')
        print('-' * 40)

print('<< VOLTE SEMPRE >>')
