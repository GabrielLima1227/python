from random import choice

primeiro_aluno = input("Digite o nome do primeiro aluno: ")
segundo_aluno = input("Digite o nome do segundo aluno: ")
terceiro_aluno = input("Digite o nome do terceiro aluno: ")
quarto_aluno = input("Digite o nome do quarto aluno: ")

alunos = [primeiro_aluno, segundo_aluno,terceiro_aluno, quarto_aluno]

escolhido = choice(alunos)
print(f"O aluno escolhido para apagar o quadro foi {escolhido}")