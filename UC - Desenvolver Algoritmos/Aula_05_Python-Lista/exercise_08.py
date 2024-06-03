print("""
Enunciado do exercício:
    8. Leia um número fornecido pelo usuário. Se esse número for positivo, 
    calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
""")

numero = float(input("Digite um número: "))

if numero < 0:
    print("Número é inválido")
    exit(0)

raiz_quadrada = numero ** 0.5

print(f"A raiz quadrada de {numero} é {raiz_quadrada}")