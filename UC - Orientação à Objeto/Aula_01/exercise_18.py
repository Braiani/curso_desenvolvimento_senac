print("""
Enunciado do exercício:
    Escreva uma função que recebe um número inteiro positivo 'n' e retorna a soma de todos os números pares de 1 até 'n'.
""")

def soma_pares(delimitador):
    soma = 0
    for i in range(1, delimitador + 1):
        if i % 2 == 0:
            soma += i
    return soma

num = int(input("Digite o número máximo: "))

if num < 0:
    print("Valor inválido")
else:
    print(f"A soma dos números pares é: {soma_pares(num)}")