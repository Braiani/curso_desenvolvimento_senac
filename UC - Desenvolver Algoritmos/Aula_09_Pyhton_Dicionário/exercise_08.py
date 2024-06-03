print("""
Enunciado do exercício:
    8. Contagem de Letras:
        ○ Leia um texto e conte quantas vezes cada letra aparece. Armazene as letras e suas contagens em um dicionário.
""")

texto = input("Digite o texto: ")

letras = {}
for letra in texto:
    if letra in letras or letra == " ":
        continue
    letras[letra] = texto.count(letra)


for letra, valor in letras.items():
    print(f"'{letra}' apareceu {valor} vezes.")