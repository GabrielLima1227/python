primeira_nota = int(input("Digite a sua primeira nota: "))
segunda_nota = int(input("Digite a sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

print(f"A sua média é {media:.1}")

if media >= 7:
    print("Sua média foi boa!")
else:
    print("Sua média foi ruim, estude mais!")
