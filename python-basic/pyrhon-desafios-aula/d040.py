primeira_nota = float(input("Digite a sua primeira nota: "))
segunda_nota = float(input("Digite a sua segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7.0:
    print(f"Sua média é de {media:.1f} e você foi APROVADO!")
elif 5.0 <= media <= 6.9:
    print(f"Sua média foi de {media:.1f} e você vai para RECUPERAÇÃO!")
else:
    print(f"Sua média foi de {media:.1f} e você foi REPROVADO!")