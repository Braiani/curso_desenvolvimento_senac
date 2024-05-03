print("""
Enunciado do exercício:
    12. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
""")

numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

diferenca = 0

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"O maior número é o 1º - A diferença entre eles é {diferenca}")
elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(f"O maior número é o 2º - A diferença entre eles é {diferenca}")
else:
    print("Números iguais - Sem diferença entre eles")