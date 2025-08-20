from random import randint

valor_do_jogador = valor_do_computador = valor_total = vitorias = 0 

print("-=" * 20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=" * 20)
while True:
    valor_do_jogador = int(input("Digite um valor: "))
    valor_do_computador = randint(1,10)
    valor_total = valor_do_jogador + valor_do_computador
    par_ou_impar = ""
    while par_ou_impar not in ("P", "I"):
        par_ou_impar = input("Você quer Par ou Ímpar? [P/I] ").strip().upper()
    if par_ou_impar == "P":
        if valor_total % 2 == 0:
            print(f"Você jogou {valor_do_jogador} e o compuatdor jogou {valor_do_computador}. Total de {valor_total} deu Par")
            print("Você venceu essa rodada!")
        else:
            print(f"Você jogou {valor_do_jogador} e o compuatdor jogou {valor_do_computador}. Total de {valor_total} deu Ímpar")
            print("Você perdeu a rodada")
            break 
    elif par_ou_impar == "I":
        if valor_total % 2 != 0:
            print(f"Você jogou {valor_do_jogador} e o compuatdor jogou {valor_do_computador}. Total de {valor_total} deu Ímpar")
            print("Você venceu essa rodada!")
        else:
            print(f"Você jogou {valor_do_jogador} e o compuatdor jogou {valor_do_computador}. Total de {valor_total} deu Par")
            print("Você perdeu a rodada")
            break 
    vitorias += 1
print("-=" * 20)
print(f"GAME OVER, Você venceu {vitorias} vezes") 