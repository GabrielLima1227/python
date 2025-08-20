test = list()
test.append("Gabriel")
test.append(20)
print(test)

galera = list()
galera.append(test[:])
print(galera)

test[0] = "Guanabara"
test[1] = 41
galera.append(test[:])
print(galera)
