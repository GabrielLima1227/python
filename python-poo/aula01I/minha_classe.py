# Conceitos Básicos
class MinhaClasse:
    def __init__(self, info, elemento ): #Método Construtor
        #Uma classe pode ter atributos de qualquer tipo de dado, como int, float, str, bool, list, tuple, dict, entre outros.
        #Também é possível utilizar entradas de dados fornecidas pelo usuário para definir os valores desses atributos.
        self.atributo_1 = "Meu atributo"
        self.atributo_2 = elemento
        self.atributo_3 = [1,2,"a"]
        self.novo_atributo = info #Parâmetro que recebe entradas de dados fornecidas pelo usuário.
        print(self.novo_atributo)

    def metodo_01(self):
        print("Minha Ação 1")
        print("Minha Ação 2")
        print(self.atributo_2) #Podemos usar os atributos da nossa classe em qualquer método definido dentro dela.
        return "Olá Mundo"
    
    def metodo_2(self, numero):
        self.metodo_01() #Podemos chamar um método dentro de outro método, assim como fazemos com funções comuns.
        print(self.atributo_3[1] + numero)

#objeto        #classe -> Instanciamos um Objeto
minha_classe = MinhaClasse("Info aqui no construtor", 123)

#Atribuindo à variável o valor de retorno do método do meu objeto.
response = minha_classe.metodo_01()

print()
print(response)

print()
minha_classe.metodo_2(3)