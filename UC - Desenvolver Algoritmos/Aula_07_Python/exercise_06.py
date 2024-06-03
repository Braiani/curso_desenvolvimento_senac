print("""
Enunciado do exercício:
    6 - Leia 10 números e apresente o quadrado de cada um
""")

numeros = []

for i in range(10):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in numeros:
    print(f"O quadrado do número {i} é {i**2}")