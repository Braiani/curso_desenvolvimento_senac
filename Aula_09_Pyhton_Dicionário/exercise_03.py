print("""
Enunciado do exercício:
    3. Agenda Telefônica:
        ○ Crie um programa que permita adicionar, buscar e remover contatos de uma agenda telefônica usando um dicionário.
""")

agenda = {
    "Bob": "(67) 99999-9999",
    "Marley": "(67) 99999-9999"
}

while True:
    print("""
                         ________
                        || Menu ||
            +===============================+
            |  Código  |      Operação      |
            |----------+--------------------+
            |     a    |  Adicionar Contato |
            |----------+--------------------+
            |     b    |   Buscar Contato   |
            |----------+--------------------+
            |     r    |   Remover Contato  |
            |----------+--------------------+
            |     v    |    Ver Contatos    |
            +===============================+
            Digite qualquer coisa para sair...
          """)
    
    opcao = input("Digite a opção desejada: ").capitalize()

    if opcao == "A":
        nome = input("Digite o nome do contato: ").capitalize()
        if nome in agenda:
            print()
            print("Nome existe! Deseja atualizar o contato (digite s para sim)?")
            if input().lower() == "s":
                telefone = input("Digite o número do contato: ")
                agenda.update({nome: telefone})
        else:
            telefone = input("Digite o número do contato: ")
            agenda.update({nome: telefone})

    elif opcao == "B":
        nomeOuTelefone = input("Digite o contato ou número que deseja buscar: ").capitalize()
        if nomeOuTelefone not in agenda:
            print()
            print("Contato não existe!")
            continue
        for nome, telefone in agenda.items():
            if nome == nomeOuTelefone or telefone == nomeOuTelefone:
                print()
                print(nome,telefone,sep=": ")

    elif opcao == "R":
        nomeOuTelefone = input("Digite o contato ou número que deseja remover: ").capitalize()
        if nomeOuTelefone not in agenda:
            print()
            print("Contato não existe!")
            continue
        
        del agenda[nome]
                
    elif opcao == "V":
        print()
        print("/--------------- Agenda Telefônica ---------------\\")
        print()
        
        for nome, telefone in agenda.items():
            print(nome,telefone,sep=": ")
        
        print()
        print("/--------------- ------------------ ---------------\\")
    else:
        break