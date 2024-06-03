print("""
Enunciado do exercício:
    11. Contagem de Vogais: 
      ○ Leia um texto e conte quantas vezes cada vogal (a, e, i, o, u) aparece. Armazene as vogais e suas contagens em um dicionário.
""")

texto = input("Digite o texto: ")

palavras = {}
vogais = ['a','e','i','o','u']
for palavra in texto:
    if palavra not in vogais:
        continue
    palavras[palavra] = texto.count(palavra)

for vogal in vogais:
    print(f"'{vogal}' apareceu {palavras[vogal]} vezes.")