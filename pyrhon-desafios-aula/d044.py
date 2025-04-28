preço = float(input('preço das compras: '));
print('''
    [ 1 ] à vista dinheiro/cheque; #10% desconto
    [ 2 ] à vista cartão; #5% desconto
    [ 3 ] 2x cartão; #preço normal
    [ 4 ] 3x ou mais no cartão; #20% juros
''');
opção = int(input('opção: '));
if opção == 1:
    print(f'você optou por pagamento à vista, preço: R$ {preço - (preço*10)/100:.2f}');
elif opção == 2:
    print(f'você optou por pagamento à vista no cartão, preço: R$ {preço - (preço*5)/100:.2f}');
elif opção == 3:
    print('você optou por pagamento 2x no cartão, preço: R$',preço)
elif opção == 4:
    print(f'você optou por pagamento 3x ou mais no cartão com 20% juros.');
    parcelas = int(input('Quantas parcelas: '));
    print(f'parcelado em {parcelas}x será {(preço+(preço*20)/100)/parcelas} por mês, preço: R$ {preço + (preço*20)/100:.2f}');
else:
    print('opção incorreta.')