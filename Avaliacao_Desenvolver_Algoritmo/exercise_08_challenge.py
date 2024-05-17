print("---- Bem vindo ao sistema do Mercado Senac Hub Academy ----")

usuarios = [
    ['admin', '123', 'adm', [
        '123456', 'Administrador', '10/02/1990', '123.456.789-00'
    ]], 
    ['usuario', '321', 'cli', [
        '321.456.789-00', 'Usuário 1'
    ]],
    ['user', '654', 'cli', [
        '123.654.789-00', 'Usuário 2'
    ]]
]

produtos = [
    'Produtos para Casa', [
        'Limpeza', [
            ['1001', 'Vassoura', 'Produto necessário para tirar o pó', 12.50],
            ['1002', 'Rodo', 'Produto necessário para tirar a água', 10.50],
            ['1003', 'Pano', 'Produto necessário usar com o Rodo', 2],
        ],
        'Decoração', [
            ['1004', 'Quadro', 'Um lindo retrato de animal', 120],
            ['1005', 'Vaso de planta', 'Um lindo vaso de samambaia', 65.8],
        ]
    ]
]

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
            |     A    |  Atualizar Estoque |
            |----------+--------------------+
            |     C    | Cadastrar Produtos |
            |----------+--------------------+
            |     V    |  Verificar Estoque |
            |----------+--------------------+
            |     0    |       Sair         |
            +===============================+
        """)

        opcao_usuario = input("Digite a opção escolhida: ")

        if opcao_usuario == "0":
            break
        elif opcao_usuario == "V":
            print(produtos)
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
            |----------+--------------------+
            |     0    |       Sair         |
            +===============================+
        """)
        opcao_usuario = input("Digite a opção escolhida: ")

        if opcao_usuario == "0":
            break
        else:
            print("Opção inválida!")