print("""
Enunciado do exercício:
    7 - Crie 2 listas vazias, no primeiro leia 5 números e armazene o valor digita multiplicado por 5 na segunda lista. Apresente o resultado ao final.
""")

numeros = []
numeros_multiplicados = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    numeros_multiplicados.append(num * 5)

print(f"A lista digitada foi: {numeros}")
print(f"Os múltiplos por 5 são: {numeros_multiplicados}")