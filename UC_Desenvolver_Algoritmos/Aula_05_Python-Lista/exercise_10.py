print("""
Enunciado do exercício:
    10. Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
        • O número digitado ao quadrado;
        • A raiz quadrada do número digitado;
""")

numero = int(input("Digite um número inteiro: "))

quadrado = 0
raiz_quadrada = 0

if numero >= 0:
    quadrado = numero ** 2
    raiz_quadrada = numero ** 0.5

    print(f"• O número digitado ao quadrado: {quadrado}")
    print(f"• A raiz quadrada do número digitado: {raiz_quadrada}")