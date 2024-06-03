print("""
Enunciado do exercício:
    24. Crie um programa que calcule e mostre a área de um trapézio. Lembre-se a base maior e a base menor devem ser números maiores que zero.
""")

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura do trapézio: "))
area = 0

if base_maior < 0 or base_menor < 0 or altura < 0:
    print("Dados inválidos!")
    exit()

area = ((base_maior + base_menor) * altura) / 2

print(f"A área do trapézio é {area}")