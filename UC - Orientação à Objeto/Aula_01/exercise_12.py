print("""
Enunciado do exercício:
    Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. 
    Por exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).
""")

def soma_algatismos(numero):
    soma = 0
    for i in str(numero):
        soma += int(i)

    return soma

numero = int(input("Digite um número: "))

print(f"A soma dos algarismos do número {numero} é {soma_algatismos(numero)}")