print("""
Enunciado do exercício:
    Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma função que verifica se esse triângulo existe ou não.
    Para que um triângulo exista, cada lado deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos outros dois lados.
""")

def lado_maior(a, b, c):
    if a >= (b + c):
        return True
    return False

def modulo_lados(num1, num2):
    if num1 > num2:
        return num1 - num2
    elif num2 > num1:
        return num2 - num1
    else:
        return 0

def existe_triangulo(lado1, lado2, lado3):
    if lado_maior(lado1, lado2, lado3) or lado1 <= modulo_lados(lado2, lado3):
        print("Triângulo não existe!")
    elif lado_maior(lado2, lado1, lado3) or lado2 <= modulo_lados(lado1, lado3):
        print("Triângulo não existe!")
    elif lado_maior(lado3, lado1, lado2) or lado3 <= modulo_lados(lado2, lado1):
        print("Triângulo não existe!")
    else:
        print("Existe!")


print("Vamos pegar os dados: ")

existe_triangulo(float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: ")))