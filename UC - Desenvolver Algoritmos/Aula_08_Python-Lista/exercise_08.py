print("""
Enunciado do exercício:
    8. Faça um programa que leia 5 números e informe a soma e a média
""")

numeros = []

for i in range(5):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

print(f"A soma dos números digitado foi {sum(numeros)}")
print(f"A média dos números digitado foi {sum(numeros)/len(numeros)}")