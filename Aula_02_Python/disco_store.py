def precos_produtos():
    return [
        ["Azul", 20.0],
        ["Laranja", 30.0],
        ["Roxo", 40.0],
        ["Marrom", 50.0],
        ["Vermelho", 60.0]
    ]

def preco_por_cor(cor):
    valores = precos_produtos()
    for cor_array in valores:
        if cor_array[0] == cor:
            return cor_array[1]
    return False

def print_menu_precos():
    valores = precos_produtos()
    print("||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=")
    for produto in valores:
        print(f"     Etiqueta: {produto[0]} - Valor: R$ {produto[1]}")
    print("||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=||-=-=-=-=", end="\n\n")

cart_itens = 0
cart_value = 0

while True:
    print_menu_precos()
    cor_digitada = input("Digite a cor da etiqueta (Digite Sair para finalizar): ").capitalize()
    if cor_digitada == "Sair":
        break
    if not preco_por_cor(cor_digitada):
        print("Valor não localizado!")
        print()
        continue
    valor_escolhido = preco_por_cor(cor_digitada)
    print(f"O valor do produto pesquisado é R$ {valor_escolhido}")
    escolha = input("Deseja adicionar ao carrinho? (S/N)").capitalize()
    if escolha == "N":
        print("O item foi descartado!")
        print()
        continue
    quantidade = int(input("Qual a quantidade de discos você deseja acrescentar? "))
    cart_itens = cart_itens + quantidade
    cart_value = cart_value + (quantidade * valor_escolhido)
    print(f"O valor de R$ {(quantidade * valor_escolhido)} foi adicionado ao seu carrinho. Sua compra total é R$ {cart_value} - Com um total de {cart_itens} itens.")

print()
print(f"Sua compra total é R$ {cart_value} - Com um total de {cart_itens} itens.")