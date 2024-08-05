print("""
Enunciado do exercício:
    2 - Crie um array com 10 números e some eles utilizando o FOR
""")
import random
# lista = input("Digite os números separados por ',': ").split(',')

lista = []
for i in range(10):
    lista.append(random.randint(1, 300))

soma = 0

for item in lista:
    soma += int(item)

print(f"A soma da lista {lista} é {soma}")