print("""
Enunciado do exercício:
    13. Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem: Números iguais.
""")

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

if numero1 > numero2:
    print(f"O 1º número ({numero1}) é maior.")
elif numero2 > numero1:
    print(f"O 2º número ({numero2}) é maior.")
else:
    print("Os números são iguais")