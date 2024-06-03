print("""
Enunciado do exercício:
    Faça um programa que peça um número inteiro positivo 'n' ao usuário e imprima um quadrado de lado 'n' preenchido com hashtags. Por exemplo, para n=4
""")

def print_quadrado(n):
    for i in range(n):
        print("#"*n)

print_quadrado(int(input("Digite quantos quadrados deseja: ")))