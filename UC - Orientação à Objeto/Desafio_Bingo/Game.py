from Roleta import Roleta
from time import sleep
from Cartela import Cartela

def exibir_menu():
    print("======= Menu Principal =======")
    print("1. Girar o Globo do Bingo")
    print("2. Exibir minha Cartela")
    print("3. Exibir números sorteados")
    print("4. Jogar bingo com outra pessoa")
    print("5. Gerar nova cartela")
    print("6. Sair")
    print("==============================")

def multiplayer():
    print("Seja bem vindo ao jogo multiplayer!")

    while True:
        cartela.mostrarCartela()

        try:
            sorteado = int(input("Digite o número sorteado: (ctrl + c para sair) "))
            cartela.salvarNumeroSorteado(sorteado)
            if cartela.verificarCartelaBingada():
                print("\n\n\n\n")
                print("Você ganhou!!!")
                print("Grite BINGOOOOOOOOOOOOOOOO!!!")
                print("\n\n\n\n")
        except KeyboardInterrupt:
            print()
            print("Obrigado por usar nosso modo on-line!")
            print()
            break

def principal():
    global cartela
    cartela = Cartela()

    sorteados = []
    roleta = Roleta()

    contador = 0
    
    cartela.mostrarCartela()
    print()
    
    while True:
        exibir_menu()
        
        try:
            escolha_usuario = int(input("Digite a opção desejada: "))
            if escolha_usuario not in range(1,7):
                raise ValueError
            
            if escolha_usuario == 6:
                raise KeyboardInterrupt
            
            if escolha_usuario == 2:
                print()
                print()
                cartela.mostrarCartela()
                print()
            
            if escolha_usuario == 3:
                print()
                print()
                print(f"Os números sorteados até o momento foram: {sorteados}")
                roleta.exibir_historico()
                print()

            if escolha_usuario == 1:
                print("Girandooooo......")
                numero_sorteado = roleta.girar()
                sorteados.append(numero_sorteado)
                contador += 1
                cartela.salvarNumeroSorteado(numero_sorteado)
                sleep(1)
                print()

                if numero_sorteado <= 15:
                    numero_sorteado = "B " + str(numero_sorteado)
                elif numero_sorteado <= 30:
                    numero_sorteado = "I " + str(numero_sorteado)
                elif numero_sorteado <= 45:
                    numero_sorteado = "N " + str(numero_sorteado)
                elif numero_sorteado <= 60:
                    numero_sorteado = "G " + str(numero_sorteado)
                elif numero_sorteado > 60:
                    numero_sorteado = "O " + str(numero_sorteado)
                

                if contador < 5:
                    print(f"O número sorteado foi.... {numero_sorteado}")
                    print()
                else:
                    print(f"O número sorteado foi....")
                    sleep(1)
                    print(f"Fooiii....")
                    sleep(1)
                    print(f"Quem está na boa aí?!?!?!....")
                    sleep(2)
                    print(f"O número sorteado foi.... {numero_sorteado}")
                    print()

                if cartela.verificarCartelaBingada():
                    print("\n\n\n\n")
                    print("Você ganhou!!!")
                    print("Grite BINGOOOOOOOOOOOOOOOO!!!")
                    print("\n\n\n\n")
            
            if escolha_usuario == 4:
                multiplayer()

            if escolha_usuario == 5:
                cartela.gerarNovaCartela()
                cartela.mostrarCartela()

        except KeyboardInterrupt:
            print()
            print("Obrigado por usar nosso sistema!!")
            print()
            exit()
        except ValueError:
            print("Opção inválida!")
            continue


if __name__ == '__main__':
    principal()