print("""
Enunciado do exercício:
    18. Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
      utilizando as seguintes formulas (onde h corresponde à altura):
        • Homens: (72.7 * h) - 58
        • Mulheres: (62,1 * h) - 44,7
""")

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo (F/M): ").capitalize()

peso_ideal = 0

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
elif sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    print("Dados inválidos!")
    exit()

print("Seu peso ideal é", peso_ideal)