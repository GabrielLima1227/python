def escreva(texto):
    print(("-" * len(texto)))
    print(f"{texto}")
    print(("-" * len(texto)))

escreva("Abóbora de Halloween")

#Ou

def escreva(texto):
    texto.split(",")
    print(("-" * len(texto)))
    print(''.join(texto))
    print(("-" * len(texto)))

escreva("Jujutsu Kaisen")

# Ou
def escreva(texto):
    texto.split(",")
    def linha():
        print(("-" * len(texto)))
    linha()
    print(''.join(texto))
    linha()

escreva("Não Conheci O Outro Mundo Por Querer")