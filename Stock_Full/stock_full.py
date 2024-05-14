import time
def cadastrar_produto(operacao, produto, quantidade, banco):
    estoque = open(banco, 'a')
    if operacao == 'cadastrar':
        estoque.write(produto + ":" + quantidade)

def listar_produtos(banco):
    try:
        estoque = open(banco, 'r')
        for produto in estoque.readlines():
            print(f"Código: {produto}")
        
    except FileNotFoundError:
        print("Banco de dados não localizado!")
        time.sleep(2)

def clear():
    print("\033c", end="")


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
|     S    |       Sair         | Encerra a execução do programa.                                       |
+=======================================================================================================+
""")
    operacao = input("Digite o código da operação que deseja realizar: ").capitalize()

    if operacao == "S":
        break
    elif operacao == "L":
        listar_produtos(banco_dados)

clear()
print("\nObrigado por utilizar nossos serviços!")