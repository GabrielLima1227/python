def area(largura, coprimento):
    resultado = largura * coprimento
    print(f"A área de um terreno {largura:.1f}m x {coprimento:.1f}m é de {resultado}m²")


#Programa principal 
print("\t CONTROLE DE TERRENOS")
print("-" * 60)
largura = float(input("Largura (M): "))
comprimento = float(input("Comprimento (M): "))
area(largura, comprimento)  