print("""
Enunciado do exercício:
    7. Faça um programa que leia 5 números e informe o maior número. 
""")

numeros = []

for i in range(5):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

print(f"O maior número digitado foi {max(numeros)}")