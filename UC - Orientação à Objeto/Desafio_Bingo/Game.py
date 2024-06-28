from Roleta import Roleta
from time import sleep
from Cartela import Cartela

def exibir_menu():
    print("======= Menu Principal =======")
    print("1. Girar o Globo do Bingo")
    print("2. Exibir minha Cartela")
    print("3. Exibir números sorteados")
    print("4. Jogar bingo com outra pessoa")
    print("5. Sair")
    print("==============================")

def formatar_numero(num):
    if num < 10:
        return f"0{num}"
    return num

def mostrar_cartela():
    print("Veja abaixo sua cartela: ")
    print()
    print(f"+{'-'*78}+")
    print("|\t B\t||\t I\t||\t N\t||\t G\t||\t O\t|")
    print(f"+{'-'*78}+")
    for i in range(5):
        print(f"|\t{formatar_numero(cartela["B"][i])}\t|", end="")
        print(f"|\t{formatar_numero(cartela["I"][i])}\t|", end="")
        if i != 2:
            print(f"|\t{formatar_numero(cartela["N"][i])}\t|", end="")
        else:
            print(f"|     Free     |", end="")
        print(f"|\t{formatar_numero(cartela["G"][i])}\t|", end="")
        print(f"|\t{formatar_numero(cartela["O"][i])}\t|")
        print(f"|{"-"*15}||{"-"*14}||{"-"*14}||{"-"*14}||{"-"*13}|")

def multiplayer():
    pass

def principal():
    global cartela
    cartela = Cartela().gerar_cartela()

    sorteados = []
    roleta = Roleta()
    
    
    while True:
        exibir_menu()
        
        try:
            escolha_usuario = int(input("Digite a opção desejada: "))
            if escolha_usuario not in range(1,6):
                raise ValueError
            
            if escolha_usuario == 5:
                raise KeyboardInterrupt
            
            if escolha_usuario == 2:
                print()
                print()
                mostrar_cartela()
                print()
            
            if escolha_usuario == 3:
                print()
                print()
                print(f"Os números sorteados até o momento foram: {sorteados}")
                roleta.exibir_historico()
                print()

            if escolha_usuario == 1:
                print("Girandooooo......")
                while True:
                    numero_sorteado = roleta.girar()
                    if numero_sorteado not in sorteados:
                        sorteados.append(numero_sorteado)
                        sleep(2)
                        print()
                        print(f"O número sorteado foi.... {numero_sorteado}")
                        print()
                        break
            
            if escolha_usuario == 4:
                multiplayer()

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