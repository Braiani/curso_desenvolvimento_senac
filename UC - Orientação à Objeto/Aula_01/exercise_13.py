print("""
Enunciado do exercício:
    Crie um programa que pede ao usuário para digitar uma sequência de números e, em seguida, calcula a média aritmética desses números.
""")

def calcula_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas)/len(notas)

notas = []

while True:
    try:
        nota = float(input("Digite um nota (F para finalizar): "))

        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida")

    except:
        break

media = calcula_media(notas)

print(f"A média das notas {notas} é: {media}")