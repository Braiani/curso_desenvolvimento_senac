print("""
Enunciado do exercício:
    18. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120
""")

n = int(input("Digite o n do fatorial: "))
fatorial = n
n -= 1

while n > 0:
    fatorial *= n
    n -= 1

print(f"Resultado do fatorial: {fatorial}")