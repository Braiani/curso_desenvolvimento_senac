print("""
Enunciado do exercício:
    14. Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem crescente.
      Caso contrário, imprima não está em ordem crescente.
""")

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if num1 < num2 and num2 < num3:
    print("Crescente!")
else:
    print("NÃO ESTÃO em ordem crescente!")