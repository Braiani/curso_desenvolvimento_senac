#!/usr/bin/env python3
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
        print_and_sleep(f"Ocorreu um erro: {error}", 1)
        if input("Digite 0 para tentar novamente... ") == "0":
            cadastrar_produto(banco)


def pesquisar_produto_por_codigo(banco, codigo, error=True):
    try:
        retorno = False
        produtos = open(banco, 'r')

        for produto in produtos.readlines():
            if produto.strip().split(',')[0] == codigo:
                retorno = produto.strip().split(',')

        produtos.close()
        return retorno
    except FileNotFoundError:
        if error:
            print_and_sleep("Banco de dados não localizado!")


def cadastrar_produto_banco(codigo, produto, quantidade, banco):
    try:
        estoque = open(banco, 'a')
        estoque.write(f"{codigo},{produto},{str(quantidade)}\n")
        estoque.close()
        print_and_sleep("Produto cadastrado com sucesso!", 1)
    except Exception as error:
        print_and_sleep(f"Ocorreu um erro: {error}", 2)


def listar_produtos(banco):
    listar_produtos_banco(banco)
    input("Pressione enter para retornar ao menu... ")


def listar_produtos_banco(banco):
    try:
        estoque = open(banco, 'r')

        print("+========================================================+")
        for produto in estoque.readlines():
            prod = produto.strip().split(',')
            print(f"| Código: {prod[0]}")
            print(f"| Descricao: {prod[1]}")
            print(f"| Quantidade em estoque: {prod[2]}")
            print("+--------------------------------------------------------+")

        print("+========================================================+")
        estoque.close()

    except FileNotFoundError:
        print_and_sleep("Banco de dados não localizado!")


def entrada_estoque(banco):
    codigo = input("Digite o código do produto: ")
    pesquisar_produto = pesquisar_produto_por_codigo(banco, codigo)
    if pesquisar_produto:
        print(f"A quantidade atual em estoque do produto {pesquisar_produto[1]} é {pesquisar_produto[2]}")
        quantidade = float(input("Digite a quantidade que está entrando no estoque: "))
        movimenta_estoque_banco(codigo, quantidade, banco)
        print_and_sleep("Estoque atualizado!", 2)
    else:
        print_and_sleep("Produto não encontrado! Cadastrar produto (S/N)?", 1)
        if input().capitalize() == "S":
            cadastrar_produto(banco)


def movimenta_estoque_banco(codigo, quantidade, banco):
    estoque = open(banco, 'r')
    produtos = []
    for produto in estoque.readlines():
        prod = produto.strip().split(',')
        if prod[0] == codigo:
            if (float(prod[2]) + quantidade) < 0:
                print_and_sleep("Estoque não pode ser negativo!", 2)
                return
            produtos.append(f"{prod[0]},{prod[1]},{str(float(prod[2]) + quantidade)}\n")
            verificar_limites_estoque(float(prod[2]) + quantidade)
        else:
            produtos.append(produto)

    estoque.close()
    estoque = open(banco, 'w')
    estoque.writelines(produtos)
    estoque.close()


def saida_estoque(banco):
    codigo = input("Digite o código do produto: ")
    pesquisar_produto = pesquisar_produto_por_codigo(banco, codigo)
    if pesquisar_produto:
        print(f"A quantidade atual em estoque do produto {pesquisar_produto[1]} é {pesquisar_produto[2]}")
        quantidade = float(input("Digite a quantidade que está saindo do estoque: "))
        movimenta_estoque_banco(codigo, (quantidade * -1), banco)
        print_and_sleep("Estoque atualizado!", 2)
    else:
        print_and_sleep("Produto não encontrado! Cadastrar produto (S/N)?", 1)
        if input().capitalize() == "S":
            cadastrar_produto(banco)


def verificar_limites_estoque(quantidade):
    limite_min = 3
    limite_max = 20
    if quantidade < limite_min:
        print_and_sleep("Estoque abaixo do limite mínimo!", 2)
        return False
    elif quantidade > limite_max:
        print_and_sleep("Estoque acima do limite máximo!", 2)
        return False


def verificar_estoque_banco(banco):
    try:
        print()
        count = 0
        limite_min = 3
        limite_max = 20
        estoque = open(banco, 'r')
        for produto in estoque.readlines():
            prod = produto.strip().split(',')
            if float(prod[2]) < limite_min:
                print_and_sleep(f"Produto {prod[1]} com estoque abaixo do limite mínimo! Quantidade atual: {prod[2]}", 2)
                print("-----------------------------------------------------------------------------------------------")
                count += 1
            elif float(prod[2]) > limite_max:
                print_and_sleep(f"Produto {prod[1]} com estoque acima do limite máximo! Quantidade atual: {prod[2]}", 2)
                print("-----------------------------------------------------------------------------------------------")
                count += 1
        estoque.close()

        if count == 0:
            print_and_sleep("Todos os produtos estão dentro dos limites!", 2)

        input("Pressione enter para retornar ao menu... ")
    except FileNotFoundError:
        print_and_sleep("Banco de dados não localizado!")


def clear():
    print("\033c", end="")


def print_and_sleep(txt, tempo=2):
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
|     V    |  Verificar Estoque | Verifica se algum produto está com estoque abaixo do limite mínimo    |
|----------+--------------------+-----------------------------------------------------------------------|
|     0    |       Sair         | Encerra a execução do programa.                                       |
+=======================================================================================================+
""")
    operacao = input("Digite o código da operação que deseja realizar: ").capitalize()

    if operacao == "E":
        print_and_sleep("Caregando.....", 1)
        entrada_estoque(banco_dados)
    elif operacao == "C":
        print_and_sleep("Caregando.....", 1)
        cadastrar_produto(banco_dados)
    elif operacao == "S":
        print_and_sleep("Caregando.....", 1)
        saida_estoque(banco_dados)
    elif operacao == "L":
        print_and_sleep("Caregando.....", 1)
        listar_produtos(banco_dados)
    elif operacao == "V":
        print_and_sleep("Caregando.....", 1)
        verificar_estoque_banco(banco_dados)
    elif operacao == "0":
        break
    else:
        print_and_sleep("Código digitado inválido!")

clear()
print("\nObrigado por utilizar nossos serviços!", end="\n\n")
