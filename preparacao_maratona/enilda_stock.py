'''
Gerenciador de Estoque de Supermercado:
Você é o gerente de um supermercado e precisa criar um sistema para gerenciar o estoque de produtos. 
Desenvolva um programa em python utilizando listas que permita adicionar, remover e exibir os produtos em estoque.
'''
estoque = []

def imprimir_menu():
    print("""
+========================================================================================================+
|                                   Stock Full - Utilize o menu abaixo                                   |
+========================================================================================================+
|  Código  |      Operação      |                                Ação                                    |
|----------+--------------------+------------------------------------------------------------------------|
|     C    | Cadastrar Produtos | Cadastra um novo produto com a informação de nome e a quantidade       |
|----------+--------------------+------------------------------------------------------------------------|
|     L    |  Listar Produtos   | Imprime a lista de produtos com as quantidades atuais de cada produto  |
|----------+--------------------+------------------------------------------------------------------------|
|     R    |  Remover Produtos  | Remove um produto com as quantidades da lista                          |
|----------+--------------------+------------------------------------------------------------------------|
|     0    |       Sair         | Encerra a execução do programa.                                        |
+========================================================================================================+
""")

def cadastrar_produto():
    produto = []
    try:
        produto.append(input("Digite o nome do produto: "))
        produto.append(int(input("Digite a quantidade de produtos: ")))
        estoque.append(produto)
    except:
        print("Ocorreu um erro!")

def listar_produtos():
    for produto in estoque:
        print(f"Produto: {produto[0]} - Quantidade: {produto[1]}")

def remover_produto():
    if len(estoque) == 0:
        print("Não há produtos para excluir!")
        return
    
    i = 0
    for produto in estoque:
        print(f"({i + 1}) Produto: {produto[0]} - Quantidade: {produto[1]}")
        i += 1
    try:
        produto_remover = int(input("Digite o número do produto que deseja remover: "))
        del estoque[produto_remover - 1]
        print('Lista atual: ')
        listar_produtos()
    except:
        print("Houve um erro ao tentar excluir")


while True:
    imprimir_menu()
    opcao = input("Digite a opção: ").capitalize()
    if opcao == "0":
        break
    if opcao == "C":
        cadastrar_produto()
    elif opcao == "L":
        listar_produtos()
    elif opcao == "R":
        remover_produto()
    else:
        print("Opção inválida!")