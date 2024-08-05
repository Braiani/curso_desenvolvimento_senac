print("""
Enunciado do exercício:
    5 - Crie uma lista vazia e utilizando a estrutura FOR, preencha com 10 itens de mercado e imprima ao final
""")

itens_mercado = []

for i in range(10):
    itens_mercado.append(input(f"Digite o {i+1}º item a ser adicionado: "))

print('Os itens adicionados foram:' ,', '.join(itens_mercado))