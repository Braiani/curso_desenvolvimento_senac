def exibir_menu():
    print("======= Menu Principal =======")
    print("1. Exibir Agenda")
    print("2. Sair")
    print("==============================")

agenda = ['123456', '456789']

def exibir():
    try:
        posicao = int(input("Digite a posição que está procurando: "))
        print(f"{posicao}: {agenda[posicao]}")
    except ValueError:
        print("Digite um número")
    except IndexError:
        print("Posição não localizada!")

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