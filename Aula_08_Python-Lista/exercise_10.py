print("""
Enunciado do exercício:
    10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
""")

numeros = []
while True:
    try:
        numero1 = int(input("Digite o 1º número inteiro: "))
        numero2 = int(input("Digite o 2º número inteiro: "))
        break
    except:
        print("Digite um número inteiro")

if numero1 > numero2:
    temp = numero1
    numero1 = numero2
    numero2 = temp

for num in range(numero1, numero2):
    numeros.append(str(num))

print(f"Os números do intervalo são: {", ".join(numeros)}")