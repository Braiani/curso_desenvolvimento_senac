valor_total = 0
tempo_estacionado = 0
VALOR_BASE = 9
VALOR_ADICIONAL = 1.5
opcao = 0

while opcao != 2:
    print("""
    +---------------------------------------+
    | Bem-vindo ao estacionamento!          |
    | 1 - Calcular valor do estacionamento  |
    | 2 - Sair                              |
    +---------------------------------------+
    """)

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 2:
        print("Obrigado por utilizar nosso estacionamento!")
        break

    tempo_estacionado = int(input("Digite o tempo em minutos: "))
    if tempo_estacionado <= 15:
        valor_total = 0
    elif tempo_estacionado <= 60:
        valor_total = VALOR_BASE
    else:
        valor_total = VALOR_BASE + (tempo_estacionado // 60) * VALOR_ADICIONAL

    print(f"O valor total a ser pago é de R${valor_total:.2f}")
