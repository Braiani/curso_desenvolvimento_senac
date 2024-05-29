print("""
Enunciado do exercício:
    5. Controle de Estoque:
        ○ Crie um dicionário para controlar o estoque de produtos em uma loja. Permita adicionar, remover e atualizar a quantidade de cada produto.
""")

estoque = {
    "maçã": 100,
    "banana": 50,
    "carro": 5,
    "casa": 3,
    "cachorro": 20,
    "gato": 15,
    "livro": 80,
    "computador": 30,
    "mesa": 25,
    "cadeira": 40,
    "laranja": 70,
    "caneta": 100,
    "lápis": 120,
    "bola": 60,
    "sol": 1,
    "lua": 1,
    "estrela": 1000,
    "árvore": 10,
    "flor": 200,
    "água": 500
}


while True:
    print("""
                         ________
                        || Menu ||
            +===============================+
            |  Código  |      Operação      |
            |----------+--------------------+
            |     a    |  Adicionar Estoque |
            |----------+--------------------+
            |     b    |   Buscar Estoque   |
            |----------+--------------------+
            |     r    |   Remover Estoque  |
            |----------+--------------------+
            |     v    |     Ver Estoque    |
            +===============================+
            Digite qualquer coisa para sair...
          """)
    
    opcao = input("Digite a opção desejada: ").capitalize()

    if opcao == "A":
        nome = input("Digite o nome do produto: ").lower()
        if nome in estoque:
            print()
            print("Produto já existe! Deseja atualizar o produto (digite s para sim)?")
            if input().lower() == "s":
                quantidade = input("Digite a quantidade do produto: ")
                estoque.update({nome: quantidade})
        else:
            quantidade = input("Digite a quantidade do produto: ")
            estoque.update({nome: quantidade})

    elif opcao == "B":
        nome = input("Digite o produto que deseja buscar: ").lower()
        if nome not in estoque:
            print()
            print("Produto não existe!")
            continue
        
        print()
        print("O produto", nome, "possui", estoque[nome], "em estoque!")

    elif opcao == "R":
        nome = input("Digite o produto que deseja remover: ").lower()
        if nome not in estoque:
            print()
            print("Contato não existe!")
            continue
        
        del estoque[nome]
                
    elif opcao == "V":
        print()
        print("/--------------- Estoque de produtos ---------------\\")
        print()
        
        for nome, quantidade in estoque.items():
            print(nome,quantidade,sep=": ")
        
        print()
        print("/--------------- ------------------- ---------------\\")
    else:
        break