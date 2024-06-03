print("""
Enunciado do exercício:
    11. Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar.
""")

numero = int(input("Digite o número para saber se é par: "))

if not numero % 2:
    print("Número par")
else:
    print("Número ímpar")