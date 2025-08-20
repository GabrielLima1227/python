boletim = list()

while True:
    aluno_nome = input('Nome do aluno: ')
    nota_primeira = float(input('Nota 1: '))
    nota_segunda = float(input('Nota 2: '))
    media_aluno = (nota_primeira + nota_segunda) / 2
    boletim.append([aluno_nome, [nota_primeira, nota_segunda], media_aluno])
    
    continuar = input('Quer continuar? [S/N] ').strip().lower()
    if continuar == 'n':
        break

print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('-' * 35)

while True:
    aluno_escolhido = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno_escolhido == 999:
        print('FINALIZANDO...')
        break
    if 0 <= aluno_escolhido < len(boletim):
        print(f'Notas de {boletim[aluno_escolhido][0]} são {boletim[aluno_escolhido][1]}')

print('<<<< VOLTE SEMPRE >>>>')
