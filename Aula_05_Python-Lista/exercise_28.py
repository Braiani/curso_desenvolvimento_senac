print("""
Enunciado do exercício:
    28. Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu de opções abaixo, leia dois números reais.
      Em seguida mostre o resultado da operação entre os dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
""")

escolha = int(input("""
    Escolha uma opção:
        1- Soma de 2 números.
        2- Diferença entre 2 números (maior pelo menor).
        3- Produto entre 2 números.
        4- Divisão entre 2 números (o denominador não pode ser zero).
"""))

if escolha > 4 or escolha < 1:
    print("Opção inválida!")
    exit()

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

if escolha == 1:
    print(f"Resultado: {num1 + num2}")

elif escolha == 2:
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    print(f"Resultado: {maior - menor}")

elif escolha == 3:
    print(f"Resultado: {num1 * num2}")

elif escolha == 4:
    if num1 == 0:
        resultado = num1 / num2
    elif num2 == 0:
        resultado = num2 / num1
    else:
        resultado = num1 / num2

    print(f"Resultado: {resultado}")