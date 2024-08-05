print("""
Enunciado do exercício:
      1. Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: 
      o produto do primeiro com a metade do segundo, a soma do triplo do primeiro com o terceiro. 
      O terceiro número digitado ao cubo.
""")

num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))
num3 = float(input("Digite o 3º número real: "))

result1 = num1 * (num2 / 2)
result2 = (num1 * 3) + num3
result3 = num3 ** 3

print(f"O produto do primeiro com a metade do segundo: {result1}")
print(f"A soma do triplo do primeiro com o terceiro: {result2}")
print(f"O terceiro número digitado ao cubo: {result3}")