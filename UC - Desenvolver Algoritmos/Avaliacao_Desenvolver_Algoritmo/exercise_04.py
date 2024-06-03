print("""
Enunciado do exercício:
    4 - Faça um algoritmo que receba uma lista com 10 elementos. O algoritmo deve remover o elemento 8 e mostrar a lista após a remoção.
    O exercício deve ser feito sem utilizar as funções do
    Python de remoção.
    Exemplo de entrada:
    [5, 2, 1, 7, 9, 8, 10, 200, 12, 4]
    Exemplo de saída:
    [5, 2, 1, 7, 9, 10, 200, 12, 4]
""")

lista = [5, 2, 1, 7, 9, 8, 10, 200, 12, 4]
lista_nova = []

for i in lista:
    if i != 8:
        lista_nova.append(i)

print(f"Sua nova lista sem o 8 é {lista_nova}")