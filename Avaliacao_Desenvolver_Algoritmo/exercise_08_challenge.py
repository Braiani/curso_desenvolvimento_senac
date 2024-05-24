print("---- Bem vindo ao sistema do Mercado Senac Hub Academy ----")

usuarios = [
    ['admin', '123', 'adm', [
        '123456', 'Administrador', '10/02/1990', '123.456.789-00'
    ]], 
    ['usuario', '321', 'cli', [
        '321.456.789-00', 'Usuário 1'
    ]],
    ['user', '123', 'cli', [
        '123.654.789-00', 'Usuário 2'
    ]]
]

produtos = [
    ['Produtos para Casa','Limpeza','1001', 'Vassoura', 'Produto necessário para tirar o pó', 12.50],
    ['Produtos para Casa','Limpeza','1002', 'Rodo', 'Produto necessário para tirar a água', 10.50],
    ['Produtos para Casa','Limpeza','1003', 'Pano', 'Produto necessário usar com o Rodo', 2],
    ['Produtos para Casa','Decoração','1004', 'Quadro', 'Um lindo retrato de animal', 120],
    ['Produtos para Casa','Decoração','1005', 'Vaso de planta', 'Um lindo vaso de samambaia', 65.8],
    ['Alimentos','Carne','1006', 'Patinho', 'Corte da traseira do bovino', 29.8],
    ['Alimentos','Carne','1007', 'Frango', 'Cortes especiais', 15.5],
    ['Alimentos','Frios','1008', 'Muçarela', 'Queijo Muçarela', 7.5],
    ['Alimentos','Frios','1009', 'Presunto', 'Fatiado de presunto', 8.9]
]

carrinho = ['1006','1009','1001']

usuario_logado = []
usuario_invalido = True
funcionario = False

while usuario_invalido:
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario[0] == username and usuario[1] == password:
            usuario_logado = usuario
            print("Usuário identificado! Seja Bem vindo")
            print()
            usuario_invalido = False
    
    if usuario_invalido:
        print("Usuário e/ou senha inválido!")

if usuario_logado[2] == 'adm':
    funcionario = True

while True:
    if funcionario:
        print(f"Seja Bem-vindo {usuario_logado[3][1]}!")
        print("""
                     ________
                    || Menu ||
            +===============================+
            |  Código  |      Operação      |
            |----------+--------------------+
            |     a    |  Atualizar Estoque |
            |----------+--------------------+
            |     c    | Cadastrar Produtos |
            |----------+--------------------+
            |     v    |  Verificar Estoque |
            |----------+--------------------+
            |     0    |       Sair         |
            +===============================+
        """)

        opcao_usuario = input("Digite a opção escolhida: ")

        if opcao_usuario == "0":
            break
        elif opcao_usuario == "v":
            print("+------------------------------------------------------------------------------+")
            for produto in produtos:
                print(f"Categoria: {produto[0]}")
                print(f" -- Subcategoria: {produto[1]}")
                print(f" ---- Produto: ({produto[2]}) {produto[3]} - {produto[4]} - R$ {produto[5]:.2f}")
                print("+------------------------------------------------------------------------------+")

        elif opcao_usuario == 'c':
            while True:
                categoria = input("Digite a categoria do produto: ")
                subcategoria = input("Digite a subcategoria do produto: ")
                codigo = input("Digite o código do produto: ")
                existe = False

                for produto in produtos:
                    if produto[2] == codigo:
                        existe = True
                
                if existe:
                    print("Código existente!")
                    if input("Digite 0 para cadastrar novamente... ") != "0":
                        break
                    else:
                        continue
                
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                valor = float(input("Digite o valor do produto: "))

                produtos.append([categoria, subcategoria, codigo, nome, descricao, valor])

                if input("Digite 0 para cadastrar outro produto... ") != "0":
                        break
                else:
                    continue
        
        elif opcao_usuario == 'a':
            print("+------------------------------------------------------------------------------+")
            for produto in produtos:
                print(f"Categoria: {produto[0]}")
                print(f" -- Subcategoria: {produto[1]}")
                print(f" ---- Produto: ({produto[2]}) {produto[3]} - {produto[4]} - R$ {produto[5]:.2f}")
                print("+------------------------------------------------------------------------------+")
            while True:
                codigo = input("Digite o código do produto que deseja alterar o valor: ")
                existe = False
                for produto in produtos:
                    if produto[2] == codigo:
                        print(f"Produto: ({produto[2]}) {produto[3]} - {produto[4]} - R$ {produto[5]:.2f}")
                        novo_valor = float(input("Digite o novo preço: "))
                        produto[5] = novo_valor
                        print("Valor atualizado")
                        existe = True
                
                if not existe:
                    print("Código inexistente...")

                if input("Digite 0 para atualizar o preço de outro produto... ") != "0":
                        break
                else:
                    continue

        else:
            print("Opção inválida!")


    else:
        print(f"Seja Bem-vindo {usuario_logado[3][1]}!")
        print("""
                     ________
                    || Menu ||
            +===============================+
            |  Código  |      Operação      |
            |----------+--------------------+
            |     c    |  Comprar Produto   |
            |----------+--------------------+
            |     f    |  Finalizar Compra  |
            |----------+--------------------+
            |     n    |     Nota Fiscal    |
            |----------+--------------------+
            |     r    |  Remover Produto   |
            |----------+--------------------+
            |     v    |    Ver produtos    |
            |----------+--------------------+
            |     0    |       Sair         |
            +===============================+
        """)
        opcao_usuario = input("Digite a opção escolhida: ")


        if opcao_usuario == "f":
            if len(carrinho) > 0:
                total = 0
                print("Seu carrinho de compras está assim: ")
                for item in carrinho:
                    for produto in produtos:
                        if produto[2] == item:
                            total += produto[5]
                            print(f" -- ({produto[2]}) {produto[3]} - R$ {produto[5]:.2f}")
                
                print()
                print(f"Valor total da compra: R$ {total:.2f}")

                while True:
                    print("Formas de pagamento: D - Dinheiro; P - PIX; C - Cartão")
                    forma_pagamento = input("Escolha a forma de pagamento: ").capitalize()
                    if forma_pagamento == "C":
                        print("Escolha qual o tipo do cartão: D - Débito; C - Crédito ou V - Voucher")
                        forma_cartao = input("Digite qual tipo de cartão: ").capitalize()
                        if forma_cartao != "D" and forma_cartao != "C" and forma_cartao != "V":
                            print("Tipo de cartão inválido!")
                            continue
                    
                    if forma_pagamento == "C" or forma_pagamento == "P":
                        saldo = float(input("Digite o saldo atual: "))
                        if saldo >= total:
                            print("Compra aprovada!")
                            print("Gerando NF... ")
                            i = 0
                            while i < 10**7.5:
                                i += 1
                            print("Nota gerada!")
                            total = 0
                            print("+----------------------------------------------------------------+")
                            for item in carrinho:
                                for produto in produtos:
                                    if item in produto:
                                        print(f"- ({produto[2]}) {produto[3]} - Valor do produto: R$ {produto[5]:.2f}")
                                        print(f" -- Impostos - Municipal: R$ {produto[5] * 0.05:.2f}, Estadual: R$ {produto[5] * 0.08:.2f}, Federal: R$ {produto[5] * 0.12:.2f}")
                                        print()
                                        total += produto[5]
                            print(f"Valor total da compra - R$ {total:.2f}")
                            print(f"Valor recebido - R$ {saldo:.2f}")
                            if saldo > total:
                                print(f"Seu saldo atual é de R$ {saldo - total:.2f}")
                            print("+----------------------------------------------------------------+")
                            print(f"Valor total de imposto Municipal - R$ {total * 0.05:.2f}")
                            print(f"Valor total de imposto Estadual - R$ {total * 0.08:.2f}")
                            print(f"Valor total de imposto Federal - R$ {total * 0.12:.2f}")
                            print("+----------------------------------------------------------------+")
                            print()
                            carrinho = []
                            break
                        else:
                            print("Compra recusada! Tente outr forma de pagamento!")
                    elif forma_pagamento == "D":
                        dinheiro_recebido = float(input("Digite o valor recebido: "))
                        if dinheiro_recebido >= total:
                            print(f"Compra aprovada!")
                            if dinheiro_recebido > total:
                                print(f"Seu troco é de R$ {dinheiro_recebido - total:.2f}")
                                print("Gerando NF... ")
                            i = 0
                            while i < 10**7.5:
                                i += 1
                            print("Nota gerada!")
                            total = 0
                            print("+----------------------------------------------------------------+")
                            for item in carrinho:
                                for produto in produtos:
                                    if item in produto:
                                        print(f"- ({produto[2]}) {produto[3]} - Valor do produto: R$ {produto[5]:.2f}")
                                        print(f" -- Impostos - Municipal: R$ {produto[5] * 0.05:.2f}, Estadual: R$ {produto[5] * 0.08:.2f}, Federal: R$ {produto[5] * 0.12:.2f}")
                                        print()
                                        total += produto[5]
                            print(f"Valor total da compra - R$ {total:.2f}")
                            print(f"Valor recebido - R$ {dinheiro_recebido:.2f}")
                            if dinheiro_recebido > total:
                                print(f"Seu troco é de R$ {dinheiro_recebido - total:.2f}")
                            print("+----------------------------------------------------------------+")
                            print(f"Valor total de imposto Municipal - R$ {total * 0.05:.2f}")
                            print(f"Valor total de imposto Estadual - R$ {total * 0.08:.2f}")
                            print(f"Valor total de imposto Federal - R$ {total * 0.12:.2f}")
                            print("+----------------------------------------------------------------+")
                            print()
                            carrinho = []
                            break
                        else:
                            print("Compra recusada! Tente outra forma de pagamento!")
                            continue
            else:
                print("Carrinho Vazio!")

        elif opcao_usuario == "n":
            if len(carrinho) == 0:
                print("carrinho vazio!")
            else:
                print("Gerando NF... ")
                i = 0
                while i < 10**7.5:
                    i += 1
                print("Nota gerada!")
                total = 0
                print("+----------------------------------------------------------------+")
                for item in carrinho:
                    for produto in produtos:
                        if item in produto:
                            print(f"- ({produto[2]}) {produto[3]} - Valor do produto: R$ {produto[5]:.2f}")
                            print(f" -- Impostos - Municipal: R$ {produto[5] * 0.05:.2f}, Estadual: R$ {produto[5] * 0.08:.2f}, Federal: R$ {produto[5] * 0.12:.2f}")
                            print()
                            total += produto[5]
                print(f"Valor total da compra - R$ {total:.2f}")
                print(f"Valor total de imposto Municipal - R$ {total * 0.05:.2f}")
                print(f"Valor total de imposto Estadual - R$ {total * 0.08:.2f}")
                print(f"Valor total de imposto Federal - R$ {total * 0.12:.2f}")
                print("+----------------------------------------------------------------+")
                

        elif opcao_usuario == "v":
            print("+------------------------------------------------------------------------------+")
            for produto in produtos:
                print(f"Categoria: {produto[0]}")
                print(f" -- Subcategoria: {produto[1]}")
                print(f" ---- Produto: ({produto[2]}) {produto[3]} - {produto[4]} - R$ {produto[5]:.2f}")
                print("+------------------------------------------------------------------------------+")

        elif opcao_usuario == "c":
            while True:
                print("+------------------------------------------------------------------------------+")
                categorias_apresentadas = []
                for categoria in produtos:
                    if categoria[0] in categorias_apresentadas:
                        continue
                    print(f"{len(categorias_apresentadas) + 1} - Categoria: {categoria[0]}")
                    categorias_apresentadas.append(categoria[0])
                
                categoria_selecionada = int(input("Digite o número da categoria: "))
                if categoria_selecionada < 1 or categoria_selecionada > len(categorias_apresentadas):
                    print("Categoria inválida!")
                    continue

                print()
                print("+------------------------------------------------------------------------------+")
                subcategorias_apresentadas = []
                for subcategoria in produtos:
                    if  subcategoria[1] in subcategorias_apresentadas:
                        continue
                    if categorias_apresentadas[categoria_selecionada - 1] not in subcategoria:
                        continue
                    print(f"{len(subcategorias_apresentadas) + 1} -- Subcategoria: {subcategoria[1]}")
                    subcategorias_apresentadas.append(subcategoria[1])
                
                subcategoria_selecionada = int(input("Digite o número da subcategoria: "))
                if subcategoria_selecionada < 1 or subcategoria_selecionada > len(subcategorias_apresentadas):
                    print("Subcategoria inválida!")
                    continue
                
                print()
                print("+------------------------------------------------------------------------------+")
                produtos_apresentados = []
                for produto in produtos:
                    if produto[2] in produtos_apresentados:
                        continue
                    if subcategorias_apresentadas[subcategoria_selecionada - 1] not in produto:
                        continue
                    print(f" ---- Produto: ({produto[2]}) {produto[3]} - {produto[4]} - R$ {produto[5]:.2f}")
                    produtos_apresentados.append(produto[2])
                
                produto_selecionado = input("Digite o código do produto: ")

                existe = False
                for produto in produtos:
                    if produto[2] == produto_selecionado and produto_selecionado in produtos_apresentados:
                        existe = True
                
                if not existe:
                    print("Código não existe!")
                    if input("Digite 0 para comprar outro... ") != "0":
                        break
                    else:
                        continue
                
                if produto_selecionado in carrinho:
                    print("Produto já adicionado ao carrinho!")
                else:
                    carrinho.append(produto_selecionado)

                print("Seu carrinho de compras está assim: ")
                for item in carrinho:
                    for produto in produtos:
                        if produto[2] == item:
                            print(f" -- ({produto[2]}) {produto[3]} - R$ {produto[5]:.2f}")

                if input("Digite 0 para comprar outro produto... ") != "0":
                        break
                else:
                    continue
        
        elif opcao_usuario == "r":
            print("Seu carrinho de compras está assim: ")
            for item in carrinho:
                for produto in produtos:
                    if produto[2] == item:
                        print(f" -- ({produto[2]}) {produto[3]} - R$ {produto[5]:.2f}")
            
            produto_remover = input("Digite o código do produto que deseja remover: ")

            for item in carrinho:
                if item == produto_remover:
                    carrinho.remove(item)
                    

        elif opcao_usuario == "0":
            break
        else:
            print("Opção inválida!")