print("""
Enunciado do exercício:
    Crie um software que recebe um número do usuário, passa esse valor para uma função e ela retorna o número escrito ao inverso.
    Por exemplo, se o usuário der o valor 1234, a função  deve retornar 4321.
""")

def inverter_digitos(numero):
    num_invertido = ''
    for i in range(len(numero), 0, -1):
        num_invertido += str(numero[i-1])
    
    print(f"O número invertido é {num_invertido}")

inverter_digitos(input("Digite um valor: "))