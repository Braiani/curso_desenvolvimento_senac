print("""
Enunciado do exercício:
    11. Altere o programa anterior para mostrar no final a soma dos números.
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
    numeros.append(num)

print(f"A soma dos números do intervalo é: {sum(numeros)}")