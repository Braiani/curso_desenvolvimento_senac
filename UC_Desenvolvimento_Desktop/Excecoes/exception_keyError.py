def exibir_menu():
    print("======= Menu Principal =======")
    print("1. Exibir Agenda")
    print("2. Sair")
    print("==============================")

agenda = {
    'mae': ['123456', '456789'],
    'pai': ['123'],
    'irma': ['658']
}

def exibir():
    try:
        nome = input("Digite o nome que está procurando: ")
        print(f"{nome}: {agenda[nome][0]}")
    except KeyError:
        print("Pessoa não localizada!")

while True:
    try:
        exibir_menu()
        escolha = int(input("Escolha a sua opção: "))
        if escolha == 1:
            exibir()
        elif escolha == 2:
            raise KeyboardInterrupt
        else:
            print('Escolha inválida!')

    except KeyboardInterrupt:
        print()
        print("Fechando o sistema...")
        exit()