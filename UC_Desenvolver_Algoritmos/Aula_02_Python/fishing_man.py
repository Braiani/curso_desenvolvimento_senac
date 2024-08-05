def calcula_excesso(peso):
    VALOR_PESO_REGULAMENTO = 50
    if peso > 50:
        return peso - 50
    return 0

def calcula_multa(excesso):
    VALOR_MULTA = 4
    if excesso > 0:
        return excesso * VALOR_MULTA
    return 0

print(
    """
    +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
    |                                       |
    |     Bem vindo ao Sistema de cálculo   |
    |         de multas por excesso         |
    |                 de peso               |
    |                                       |
    +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
    """)
excesso = 0
multa = 0
pescado_total = 0

while True:
    peso_peixe = input("Digite o peso do seu pescado: (Digite Sair para encerrar) ")

    if (peso_peixe.lower() == "sair"):
        break
    pescado_total += int(peso_peixe)
    excesso_pescado = calcula_excesso(int(peso_peixe))
    multa += calcula_multa(excesso_pescado)
    excesso += excesso_pescado

print(f"Você pescou um total de {pescado_total}Kg de peixe!")
print(f"Do seu total de peixe, você teve {excesso}Kg de excesso de peixe!")
print(f"O seu excesso de peso gerou uma multa de R$ {float(multa)}!")