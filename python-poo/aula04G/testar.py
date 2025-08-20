from Conta import *

minha_conta = Conta()

minha_conta.estatisticas_da_conta()

print()
minha_conta.setter_dono("Gabriel")
minha_conta.setter_num_conta(1227)
minha_conta.setter_tipo("CP")
minha_conta.abrir_conta()
minha_conta.estatisticas_da_conta()

print()
minha_conta.deposito(75)
minha_conta.estatisticas_da_conta()

print()
minha_conta.setter_saldo(0)
minha_conta.fechar_conta()
minha_conta.estatisticas_da_conta()

print()
minha_conta.deposito(75)

print()
minha_conta.abrir_conta()
minha_conta.sacar(151)
minha_conta.estatisticas_da_conta()

print()
minha_conta.pagar_mensalidade()
minha_conta.estatisticas_da_conta()

print()
minha_conta.setter_tipo("CC")
minha_conta.pagar_mensalidade()
minha_conta.estatisticas_da_conta()

print()
minha_conta.setter_saldo(11)
minha_conta.pagar_mensalidade()
minha_conta.estatisticas_da_conta()

print()
minha_conta.setter_saldo(0)
minha_conta.fechar_conta()

print()
minha_conta.pagar_mensalidade()
minha_conta.estatisticas_da_conta()