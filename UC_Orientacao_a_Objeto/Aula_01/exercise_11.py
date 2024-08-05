print("""
Enunciado do exercício:
    Crie um programa que recebe um número inteiro positivo 'n' e calcula o fatorial desse número.
    O fatorial de 'n' é o produto de todos os números inteiros positivos de 1 até 'n'. 
    Por exemplo, 5! = 5⋅4⋅3⋅2⋅1 = 120
""")

def fatorial(n):
    total = n
    n -= 1
    for i in range(n, 1, -1):
        total *= i
    
    return total
    

numero = int(input("Digite o número para calcular o fatorial: "))

print(f"O fatorial de {numero} é {fatorial(numero)}")