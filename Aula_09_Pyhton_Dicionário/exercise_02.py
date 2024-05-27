print("""
Enunciado do exercício:
    2. Média de Notas:
        ○ Crie um dicionário com nomes de alunos e suas notas. Calcule a média das notas e exiba o resultado.
""")

alunos = {
    ('Bob', 6, 5.8, 7),
    ('John', 7, 8, 10),
    ('Marley', 10, 5.5, 9),
    ('Doe', 8.7, 9, 5.8)
}

i = 1
for aluno in alunos:
    print(f"{i} - {aluno[0]}")
    i += 1

aluno_escolhido = int(input("Digite o número do aluno: "))

i = 1
for aluno in alunos:
    if aluno_escolhido == i:
        media = (aluno[1] + aluno[2] + aluno[3])  / 3
        print(f"A média do aluno {aluno[0]} é {media}")
    i += 1