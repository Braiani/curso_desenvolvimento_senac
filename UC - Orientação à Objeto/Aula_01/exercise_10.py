print("""
Enunciado do exercício:
    Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número.
    Crie um programa que determine se a soma do número escolhido com um número aleatório é par ou ímpar.
""")

import random

def par_ou_impar(numero):
    return not numero % 2

num_escolhido = int(input("Digite um número: "))
num_aleatorio = random.randint(0,1500)

if par_ou_impar(num_escolhido + num_aleatorio):
    print(f"O número {num_escolhido + num_aleatorio} ({num_escolhido} somado com {num_aleatorio}) é par")
else:
    print(f"O número {num_escolhido + num_aleatorio} ({num_escolhido} somado com {num_aleatorio}) é ímpar")
