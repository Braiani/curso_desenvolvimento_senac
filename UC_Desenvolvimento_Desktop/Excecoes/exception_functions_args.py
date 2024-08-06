class OperadorMatematicoError(Exception):
    def __init__(self, *args: object):
        pass


def soma(num1: int, num2: int, operador: str) -> int:

    operadores = ['+', '-', '*', '/']
    if operador not in operadores:
        raise OperadorMatematicoError
    elif operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2

try:
    a = int(input("Digite o número 1: "))
    b = int(input("Digite o número 2: "))
    op = input("Digite o operador: ")

    resultado = soma(a,b,op)
    print(f"A soma é {resultado}")

except TypeError:
    print("Tipo de dados inválidos!")
except OperadorMatematicoError:
    print("Operado Matemático inválido!")
except ValueError:
    print("Tipo de dados inválidos!")