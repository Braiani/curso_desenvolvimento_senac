print("""
Enunciado do exercício:
    1. Contagem de Palavras:
        ○ Crie um programa que leia um texto e conte quantas vezes cada palavra aparece. Armazene as palavras e suas contagens em um dicionário.
""")

texto = input("Digite o texto: ").split(" ")

palavras = {}
for palavra in texto:
    if palavra not in palavras:
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1


print(palavras)

for i in palavras:
    print(f"'{i}' apareceu {palavras[i]} vezes.")