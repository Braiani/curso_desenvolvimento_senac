print("""
Enunciado do exercício:
    27. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se forem,
      se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
        • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
        • Chama-se equilátero o triângulo que tem três lados iguais.
        • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
        • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
""")

ladoa = float(input("Digite o 1º lado do Triângulo: "))
ladob = float(input("Digite o 2º lado do Triângulo: "))
ladoc = float(input("Digite o 3º lado do Triângulo: "))

if ladoa >= (ladob + ladoc) or ladob >= (ladoa + ladoc) or ladoc >= (ladoa + ladob):
    print("Esse não é um triângulo válido")
    exit(0)

if ladoa == ladob and ladob == ladoc:
    print("Esse triângulo é equilátero")
elif (ladoa == ladob and ladob != ladoc) or (ladob == ladoc and ladoc != ladoa) or (ladoa == ladoc and ladoc != ladob):
    print("Esse triângulo é isóceles")
else:
    print("Esse triângulo é escaleno")