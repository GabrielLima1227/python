print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedulas = 50
total_de_cedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:
            print(f'Total de {total_de_cedulas} cedulasulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_de_cedulas = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
