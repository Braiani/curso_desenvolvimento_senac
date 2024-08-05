num_alunos = int(input("Quantos alunos serão informados? "))
alunos = []
i = 0

while i < num_alunos:
    aluno = []
    i += 1
    matricula = input(f"Digite a matrícula do {i}º aluno: ")
    sexo = input(f"Digite o sexo do {i}º aluno (M/F): ")
    if sexo.upper() == "M" or sexo.upper() == "F":
        aluno.append(matricula)
        aluno.append(sexo)
    else:
        print("Dados inválidos, digite novamente!")
        i -= 1


print(alunos)