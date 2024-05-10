print("""
Enunciado do exercício:
    7 - Leia 10 números e apresente o maior número.
""")

numeros = []
for i in range(10):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
print(f"O maior número entre eles é {max(numeros)}")