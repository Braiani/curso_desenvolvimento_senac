def media(notas):
    return (int(notas[0]) + int(notas[1]) + int(notas[2])) / 3

notas = input("Digite as 3 notas separadas por ,: ").split(',')


print(f"A média do aluno foi: {media(notas)}")