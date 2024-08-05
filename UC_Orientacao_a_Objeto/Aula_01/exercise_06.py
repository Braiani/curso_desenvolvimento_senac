print("""
Enunciado do exercício:
    Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o seis é perfeito, pois: 6=1+2+3
""")

def descobrir_perfeito(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    
    if soma == numero:
        print(f"O número {numero} é perfeito!")
    else:
        print(f"O número {numero} não é perfeito!")

descobrir_perfeito(int(input("Digite o número para saber se é perfeito: ")))