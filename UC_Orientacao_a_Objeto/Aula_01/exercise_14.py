print("""
Enunciado do exercício:
    Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente.
    Por exemplo, “arara” é um palíndromo.
""")

def e_palindromo(frase):
    frase_contratio = ''
    for i in range(len(frase), 0, -1):
        frase_contratio += frase[i-1]
    return frase == frase_contratio

texto = input("Digite a palavra ou frase para saber se é Palíndromo: ")

if e_palindromo(texto):
    print(f"'{texto}' é palíndromo")
else:
    print(f"'{texto}' não é palíndromo")