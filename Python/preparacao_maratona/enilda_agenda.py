'''
Escreva um programa que faça um cadastro de clientes. Seu programa deve:
[Entrada]: receber os seguintes dados do usuário:
1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente.
[Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. [Saída]: AO FINAL, SOMENTE AO FINAL, Seu programa deve mostrar (um cliente por linha):
a) o nome completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente.
Obs: o usuário deve fazer esse procedimento para quantos clientes ELE QUISER.
Exemplo de Entrada:
Digite o nome completo do cliente (ou digite 'sair' para encerrar): Enilda Caceres
Digite o RG do cliente: 5478
Digite o CPF do cliente: 5588
Digite o telefone do cliente: 5877
Digite o nome completo do cliente (ou digite 'sair' para encerrar): sair
Exemplo de Saída:
Cadastro de Clientes:
====================
Nome: Enilda Caceres, RG: 5478, CPF: 5588, Telefone: 5877
'''
clientes = []
entrada = input("Digite o nome completo do cliente (ou digite 'sair' para encerrar): ")

while entrada != 'sair':
    cliente_atual = []
    cliente_atual.append(entrada)

    entrada = input("Digite o RG do cliente: ")
    cliente_atual.append(entrada)

    entrada = input("Digite o CPF do cliente: ")
    cliente_atual.append(entrada)

    entrada = input("Digite o telefone do cliente: ")
    cliente_atual.append(entrada)

    clientes.append(cliente_atual)
    entrada = input("Digite o nome completo do cliente (ou digite 'sair' para encerrar): ")

print("""
Cadastro de Clientes:
====================""")
for cliente in clientes:
    print(f"Nome: {cliente[0]}, RG: {cliente[1]}, CPF: {cliente[2]}, Telefone: {cliente[3]}")