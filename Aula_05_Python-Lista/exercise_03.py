print("""
Enunciado do exercício:
    3. Crie um programa que receba dois números e mostre qual deles é o maior.
""")

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))


if num1 > num2:
    print(f"O 1º número ({num1}) é maior.")
elif num2 > num1:
    print(f"O 2º número ({num2}) é maior.")
else:
    print("Os números são iguais")