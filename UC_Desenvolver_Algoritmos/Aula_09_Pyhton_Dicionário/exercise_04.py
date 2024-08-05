print("""
Enunciado do exercício:
    4. Tradutor Simples:
        ○ Crie um dicionário com algumas palavras em inglês e suas traduções em português. Peça ao usuário para digitar uma palavra em inglês e exiba a tradução
        correspondente.
""")

dicionario = {
    "apple": "maçã",
    "banana": "banana",
    "car": "carro",
    "house": "casa",
    "dog": "cachorro",
    "cat": "gato",
    "book": "livro",
    "computer": "computador",
    "table": "mesa",
    "chair": "cadeira",
    "orange": "laranja",
    "pen": "caneta",
    "pencil": "lápis",
    "ball": "bola",
    "sun": "sol",
    "moon": "lua",
    "star": "estrela",
    "tree": "árvore",
    "flower": "flor",
    "water": "água"
}

palavra = input("Digite a palavra em inglês que deseja traduzir: ").lower()

if palavra not in dicionario:
    print()
    print("Palavra não existe em nosso dicionário.")
else:
    print()
    print(f"A tradução de {palavra} é {dicionario[palavra]}")