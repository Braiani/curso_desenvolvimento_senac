print("""
Enunciado do exercício:
    4. Crie um programa que receba três números e mostre-os se estão em ordem crescente.
""")

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if num1 < num2 and num2 < num3:
    print(f"Números em ordem crescente! - [{num1}, {num2}, {num3}]")
