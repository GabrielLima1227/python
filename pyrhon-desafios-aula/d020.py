import random 

primeiro_aluno = input("Digite o nome do primeiro aluno: ")
segundo_aluno = input("Digite o nome do segundo aluno: ")
terceiro_aluno = input("Digite o nome do terceiro aluno: ")
quarto_aluno = input("Digite o nome do quarto aluno: ")

lista_aluno = [primeiro_aluno, segundo_aluno,terceiro_aluno,quarto_aluno]


print(f"A ordem de apresentação será \n {random.sample(lista_aluno,4)}")