print("""
Enunciado do exercício:
    6. Jogo de Palavras:
        ○ Crie um jogo onde o usuário digita uma palavra e o programa verifica se ela está no dicionário. Se estiver, exiba seu significado
""")

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

palavra = input("Digite a palavra que deseja conhecer o significado: ").lower()

if palavra not in dicionario:
    print()
    print("Palavra não existe em nosso dicionário.")
else:
    print()
    print(f"O significado de {palavra} é {dicionario[palavra]}")