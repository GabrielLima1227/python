def maior(*valores):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in valores:
        print(valor, end=" ")
    print(f"Foram informados {len(valores)} ao todo")
    print(f"O maior valor informado foi {max(valores)}.")

maior(1,2,3,4,5,6,7)
maior(2,4,5,3)
maior(3,4,5,) 