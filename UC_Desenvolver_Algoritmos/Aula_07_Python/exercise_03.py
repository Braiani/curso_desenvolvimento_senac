print("""
Enunciado do exercício:
    3 - Crie uma lista vazia e receba do usuário 10 valores no input, ao final exibir a quantidade de números positivos e negativos
""")

numeros = []
positivos = negativos = 0
for i in range(5):
    try:
        numero = float(input("Digite um número real: "))
        numeros.append(numero)
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    except:
        print("Não salvo!")

print(f"Total de números positivos: {positivos} | Total de números negativos: {negativos}")