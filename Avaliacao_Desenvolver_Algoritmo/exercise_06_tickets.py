print("Bem vindo ao Sistema de vendas de ingressos!")
vendas = []
while True:
    nome = input("Digite o nome do comprador: ")
    valor_ingresso = float(input("Digite valor do ingresso comprado: "))
    tipo_ingresso = input("Digite o tipo do ingresso (inteira/meia): ")
    carteirinha = ''
    if tipo_ingresso == 'meia':
        carteirinha = input("Digite o número da carteirinha de Meia entrada: ")

    vendas.append([nome, valor_ingresso, tipo_ingresso, carteirinha])

    if input("Deseja adicionar mais (s/n)? ").lower() != 's':
        break

soma = 0
print()
for venda in vendas:
    soma += venda[1]
    print(f"{venda[0]} comprou um ingresso do tipo {venda[2]}")

print()
print(f"O valor total dos ingressos foi R$ {soma:.2f}")