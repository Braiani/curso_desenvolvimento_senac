print("""
Enunciado do exercício:
    2 - Implemente um algoritmo em Python que receba uma string como parâmetro e imprima as vogais dessa string. 
      Exemplo: string 'univesp' → deve imprimir os caracteres 'u', 'i' e 'e'.
""")

palavra = input("Digite a palavra: ")

i = 0

while i < len(palavra):
    if palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u':
        print(palavra[i])

    i += 1