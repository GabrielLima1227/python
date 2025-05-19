primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))

soma = primeiro_valor + segundo_valor
multiplicacao = primeiro_valor * segundo_valor
divisao = primeiro_valor / segundo_valor
divisao_inteira = primeiro_valor // segundo_valor
resto_da_divisao = primeiro_valor % segundo_valor
exponenciacao = primeiro_valor**segundo_valor

print(f"A soma é {soma}, o pruduto é {multiplicacao}, a divisão é {divisao:.3f}")
print(f"Divisão inteira {divisao_inteira} e Exponenciação {exponenciacao}")