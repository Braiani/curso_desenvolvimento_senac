print("""
Enunciado do exercício:
    32. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
      Categoria Idade
        Infantil 5 a 12
        Juvenil 12 a 17
        Sênior maiores de 18 anos
""")

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade < 12:
    print("Infantil")
elif idade < 18:
    print("Juvenil")
else:
    print("Sênior")