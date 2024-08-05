print("""
Enunciado do exercício:
    33. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
      O programa deve calcular o valor a ser pago por aquele lanche.
      Considere que a cada execução somente será calculado um pedido.
""")

print("""
    +-------------------------------------------+
    | Lanche          |   Código    |   Preço   |
    +-----------------+-------------+-----------+
    | Hot Dog         |    100      |   12.00   |
    | X-Salada        |    102      |   18.50   |
    | X-BACON         |    103      |   25.50   |
    | X-Burguer       |    104      |   17.00   |
    | Suco de Laranja |    105      |    9.50   |
    | Refrigerante    |    106      |    6.00   |
    +-------------------------------------------+
""")

codigo = input("Digite o código do produto: ")
quantidade = int(input("Digite a quantidade de produtos: "))

total = 0
if quantidade < 1:
    print("Quantidade inválida!")
    exit()

if codigo == "100":
    total = 12 * quantidade
elif codigo == "102":
    total = 18.5 * quantidade
elif codigo == "103":
    total = 25.5 * quantidade
elif codigo == "104":
    total = 17 * quantidade
elif codigo == "105":
    total = 9.5 * quantidade
elif codigo == "106":
    total = 6 * quantidade

print(f"O valor total foi R$ {total:.2f}")