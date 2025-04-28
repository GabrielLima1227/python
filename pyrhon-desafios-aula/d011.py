altura_da_parede =  float(input("Qual a altura da parede? "))
largura_da_parede = float(input("Qual a largura da parede? "))
area_da_parede = altura_da_parede * largura_da_parede

print(f"A sua parede tem dimensão de {altura_da_parede}X{largura_da_parede} e a sua área é {area_da_parede}m².")    
print(f"Para pintar essa parede, você precisará de {area_da_parede/2:.2f}l de tinta")