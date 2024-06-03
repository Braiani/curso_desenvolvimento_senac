print("""
Enunciado do exercício:
    Faça um programa para lançar uma moeda. Quando chamamos uma função, ela deve retornar “cara” ou “coroa”.
    Em outra função, faça 'n' lançamentos de moedas (onde 'n' é o valor que o usuário quiser) e mostre a porcentagem de vezes que deu cara e coroa.
    O que tende a acontecer se você jogar a moeda 10, 100, 1000 ou um milhão de vezes?
""")

import random as r

def lancar_moeda():
    moeda = ["Cara", "Coroa"]
    return r.choice(moeda)

def calc_porc_lanc_moed(n):
    lancamentos = {'cara': 0, 'coroa': 0}
    for i in range(n):
        if lancar_moeda() == "Cara":
            lancamentos['cara'] += 1
        else:
            lancamentos['coroa'] += 1
    porc_cara = (int(lancamentos['cara']) * 100) / n
    porc_coroa = (int(lancamentos['coroa']) * 100) / n

    print(f"Foram lançados {n} moedas. Do total sairam: {porc_cara}% cara e {porc_coroa}% coroa")

calc_porc_lanc_moed(int(input("Digite quantas moedas deseja lançar: ")))