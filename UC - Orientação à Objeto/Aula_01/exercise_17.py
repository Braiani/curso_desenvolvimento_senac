print("""
Enunciado do exercício:
    Faça um programa que verifica se um número é primo. Um número é primo se ele não possui divisores além de 1 e ele mesmo.
""")

def numero_e_primo(numero):
    if numero == 0:
        return False
    divisores = []
    for i in range(1, int(numero) + 1):
        if numero % i == 0:
            divisores.append(i)
    return len(divisores) == 2

num = float(input("Digite um número: "))

if numero_e_primo(num):
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")