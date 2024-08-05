print("""
Enunciado do exercício:
    Crie um dado em Python. A função deve sortear um número aleatório de 1 até 6. 
    Agora, faça com que o dado seja lançado 100 vezes, mil vezes e 1 milhão de vezes.
    Armazene o valor que ele forneceu em cada lançamento e mostre quantas vezes cada número foi sorteado. 
    Compare os resultados com a estatística
""")

import random as r

def rolar_dado():
    return r.randint(1,6)

def estatistica_dados(n):
    resultado = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 5: 0, 6: 0}
    result_percent ={}

    for i in range(n):
        resultado[rolar_dado()] += 1

    for chave, valor in resultado.items():
        result_percent[chave] = (valor * 100) / n

    return result_percent

def print_estatistica(resultados):
    for chave, valor in resultados.items():
        print(f"- O número {chave} saiu {valor}% das vezes")

cem = estatistica_dados(100)
mil = estatistica_dados(1000)
milhao = estatistica_dados(100000)

print("Resultados jogando 100 vezes: ")
print_estatistica(cem)
print()
print("Resultados jogando 1000 vezes: ")
print_estatistica(mil)
print()
print("Resultados jogando 100000 vezes: ")
print_estatistica(milhao)