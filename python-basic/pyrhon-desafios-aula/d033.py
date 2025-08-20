primeiro_numero = int(input("Digite o primeiro númnero: "))
segundo_numero = int(input("Digite o segundo númnero: "))
terceiro_numero = int(input("Digite o terceito númnero: "))

#Verificar o menor número
menor_numero = primeiro_numero

if segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
    menor_numero = segundo_numero
if terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
    menor_numero = terceiro_numero
    

#Verificar maior número
maior_numero = primeiro_numero
if segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    maior_numero = segundo_numero
if terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    maior_numero = terceiro_numero

print(f"O menor valor digitado foi {menor_numero}")
print(f"O maior valor digitado foi {maior_numero}")