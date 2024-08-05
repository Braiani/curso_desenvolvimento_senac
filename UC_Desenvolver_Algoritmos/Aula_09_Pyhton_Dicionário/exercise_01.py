print("""
Enunciado do exercício:
    1. Contagem de Palavras:
        ○ Crie um programa que leia um texto e conte quantas vezes cada palavra aparece. Armazene as palavras e suas contagens em um dicionário.
""")

texto = input("Digite o texto: ").split(" ")

palavras = {}
for palavra in texto:
    palavras[palavra] = texto.count(palavra)


# print(palavras)

for palavra, valor in palavras.items():
    print(f"'{palavra}' apareceu {valor} vezes.")