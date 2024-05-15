import time

def cadastrar_produto(banco):
    try:
        codigo = input("Digite o código do produto: ")

        if pesquisar_produto_por_codigo(banco, codigo, False):
            raise Exception('Código existe!')
        
        produto = input("Digite o nome do produto: ")
        quantidade = float(input("Digite a quantidade inicial em estoque: "))

        if quantidade < 0:
            raise Exception('Valor deve ser positivo!')
        
        cadastrar_produto_banco(codigo, produto, quantidade, banco)
    except Exception as error:
        printAndSleep(f"Ocorreu um erro: {error}", 1)
        if input("Digite 0 para continuar... ") == "0":
            cadastrar_produto(banco)

def pesquisar_produto_por_codigo(banco, codigo, error=True):
    try:
        retorno = False
        produtos = open(banco, 'r')

        for produto in produtos.readlines():
            if produto.strip().split(',')[0] == codigo:
                retorno = True

        produtos.close()
        return retorno
    except FileNotFoundError:
        if error:
            printAndSleep("Banco de dados não localizado!")

def cadastrar_produto_banco(codigo, produto, quantidade, banco):
    estoque = open(banco, 'a')
    estoque.write(f"{codigo},{produto},{str(quantidade)}\n")
    estoque.close()

def listar_produtos(banco):
    listar_produtos_banco(banco)
    input("Pressione enter para retornar ao menu... ")

def listar_produtos_banco(banco):
    try:
        estoque = open(banco, 'r')
        
        for produto in estoque.readlines():
            prod = produto.strip().split(',')
            print(prod)

        estoque.close()

    except FileNotFoundError:
        printAndSleep("Banco de dados não localizado!")


def entrada_estoque(banco):
    codigo = input("Digite o código do produto: ")
    if pesquisar_produto_por_codigo(banco, codigo):
        quantidade = float(input("Digite a quantidade que está entrando no estoque: "))
        entrada_estoque_banco(codigo, quantidade, banco)
    else:
        printAndSleep("Produto não encontrado! Cadastrar produto (S/N)?", 1)
        if input().capitalize() == "S":
            cadastrar_produto(banco)

def entrada_estoque_banco(codigo, quantidade, banco):
    pass # Implementar

def clear():
    print("\033c", end="")

def printAndSleep(txt, tempo=2):
    print(txt)
    time.sleep(tempo)


banco_dados = 'estoque_db.txt'

while True:

    clear()
    print("""
                                +=======================+
                                |       Stock Full      |
                                |                       |
                                | Utilize o menu abaixo |
                                +=======================+
+=======================================================================================================+
|  Código  |      Operação      |                                Ação                                   |
|----------+--------------------+-----------------------------------------------------------------------|
|     E    | Entrada do Estoque | Ler o código do produto que está entrando no estoque e a quantidade.  |
|          |                    | Atualizar o estoque do produto.                                       |
|----------+--------------------+-----------------------------------------------------------------------|
|     C    | Cadastrar Produtos | Cadastra um novo produto com a informação de estoque, descrição  e    |
|          |                    | a quantidade. Atualiza o estoque ao final.                            |
|----------+--------------------+-----------------------------------------------------------------------|
|     S    |  Saída no Estoque  | Ler o código do produto que está saindo do estoque e a quantidade.    |
|          |                    | Atualizar o estoque do produto.                                       |
|----------+--------------------+-----------------------------------------------------------------------|
|     L    |  Listar Produtos   | Imprime a lista de produtos mostrando as quantidades atuais           |
|          |                    | de cada produto.                                                      |
|----------+--------------------+-----------------------------------------------------------------------|
|     0    |       Sair         | Encerra a execução do programa.                                       |
+=======================================================================================================+
""")
    operacao = input("Digite o código da operação que deseja realizar: ").capitalize()

    if operacao == "E":
        entrada_estoque(banco_dados)
    elif operacao == "C":
        printAndSleep("Caregando.....", 1)
        cadastrar_produto(banco_dados)
    elif operacao == "S":
        printAndSleep("Saída")
    elif operacao == "L":
        listar_produtos(banco_dados)
    elif operacao == "0":
        break
    else:
        printAndSleep("Código digitado inválido!")

clear()
print("\nObrigado por utilizar nossos serviços!", end="\n\n")