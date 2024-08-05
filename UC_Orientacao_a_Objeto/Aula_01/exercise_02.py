print("""
Enunciado do exercício:
    Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma função retorna o valor da hipotenusa.
""")

def hipotenusa(lado1, lado2):
    hipotenusa = ((lado1 ** 2) + (lado2 ** 2))**0.5
    print(f"A hipotenusa desse triângulo é: {hipotenusa}")


ladoa = float(input("Digite o 1º lado menor do triângulo: "))
ladob = float(input("Digite o 2º lado menor do triângulo: "))

hipotenusa(ladoa, ladob)