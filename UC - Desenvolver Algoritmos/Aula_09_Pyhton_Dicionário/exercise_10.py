print("""
Enunciado do exercício:
    10. Jogo de Adivinhação:
        ○ Crie um dicionário com palavras e suas definições. O programa deve escolher uma palavra aleatória e pedir ao usuário para adivinhar seu significado.
""")

import random

dicionario = {
    "cachorro": "mamífero doméstico da família dos canídeos",
    "gato": "mamífero felino doméstico",
    "casa": "estrutura construída para habitação humana",
    "carro": "veículo automotor de quatro rodas",
    "maçã": "fruto comestível da macieira",
    "banana": "fruto comestível da bananeira",
    "livro": "conjunto de folhas impressas e reunidas",
    "computador": "máquina eletrônica capaz de processar dados",
    "mesa": "móvel com tampo horizontal e pernas",
    "cadeira": "assento com encosto e pernas",
    "laranja": "fruto cítrico da laranjeira",
    "caneta": "instrumento para escrever",
    "lápis": "instrumento para escrever ou desenhar",
    "bola": "objeto esférico usado em diversos esportes",
    "sol": "estrela central do sistema solar",
    "lua": "satélite natural da Terra",
    "estrela": "corpo celeste luminoso no céu noturno",
    "árvore": "planta de grande porte com tronco e galhos",
    "flor": "órgão reprodutivo das plantas com flores",
    "água": "substância líquida incolor, transparente e inodora"
}

palavra = random.choice(list(dicionario))

print("Digite o significado da palavra:", palavra, "- Sorteada aleatoriamente:")

significado = input()

if significado == dicionario[palavra]:
    print("Você acertou!")
else:
    print("Está errado!")