def recebe_sexo_aluno(index):
    while True:
        sexo = input(f"Digite o sexo do {index}º aluno (M/F): ")
        if sexo.upper() == "M" or sexo.upper() == "F":
            return sexo
        else:
            print("Dados inválidos, digite novamente!")
            print()

def recebe_altura_aluno(index):
    while True:
        altura = int(input(f"Digite a altura do {index}º aluno (em cm): "))
        if altura < 1:
            print("Dados inválidos, digite novamente!")
            print()
        return altura

def recebe_status_fisico(index):
    while True:
        situacao = int(input(f"Digite o status físico do {index}º aluno (1-bom, 2-regular, 3-ruim): "))
        if situacao < 1 and situacao > 3:
            print("Dados inválidos, digite novamente!")
            print()
        return situacao

def calcula_meninas_altas(alunos):
    ALTURA_MINIMA = 170
    meninas_altas = 0
    for aluno in alunos:
        if aluno[1].upper() == "F" and aluno[2] >= 170:
            meninas_altas += 1
    return meninas_altas

def calcula_porcentage_fisico_bom(alunos):
    alunos_M_fisico_bom = 0
    alunos_masculino = 0
    for aluno in alunos:
        if aluno[1].upper() == "M":
            alunos_masculino += 1
            if aluno[3] == 1:
                alunos_M_fisico_bom += 1
    return round((alunos_M_fisico_bom / alunos_masculino) * 100)


num_alunos = int(input("Quantos alunos serão informados? "))
alunos = []
i = 0

while i < num_alunos:
    aluno = []
    i += 1
    matricula = input(f"Digite a matrícula do {i}º aluno: ")
    aluno.append(matricula)

    aluno.append(recebe_sexo_aluno(i))
    
    aluno.append(recebe_altura_aluno(i))

    aluno.append(recebe_status_fisico(i))

    alunos.append(aluno)

print(f"O sistema tem {calcula_meninas_altas(alunos)} meninas com mais de 1.70m")
print(f"O sistema tem {calcula_porcentage_fisico_bom(alunos)}% de meninos com um físico Bom!")