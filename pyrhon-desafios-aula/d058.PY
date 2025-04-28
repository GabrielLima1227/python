from random import randint

numero_computador = randint(1, 10)
numero_jogador = contador_de_palpites = 0

print("-=" * 10)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=" * 10)

while numero_computador != numero_jogador:
    numero_jogador = int(input("Em que núemro o computador pensou? "))
    contador_de_palpites += 1 
print(f"Parabéns você acertou o número, isso lhe custou {contador_de_palpites} palpites")