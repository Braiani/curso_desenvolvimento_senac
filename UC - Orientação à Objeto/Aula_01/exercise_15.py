print("""
Enunciado do exercício:
    Escreva uma função que recebe uma string e conta quantas vogais (a, e, i, o, u) ela contém.
""")

def contar_vogais(texto, vogal):
    return texto.count(vogal)


texto = input("Digite o texto: ").lower()

vogais = ["a","e","i","o","u"]

print("O texto possui as seguintes quantidades:")
for i in range(len(vogais)):
    print(f"- {vogais[i]}: {contar_vogais(texto, vogais[i])}")