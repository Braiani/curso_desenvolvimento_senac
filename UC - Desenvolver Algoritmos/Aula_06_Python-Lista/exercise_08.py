from datetime import date
print("""
Enunciado do exercício:
    8 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
        Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
        Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
        A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
    Faça um programa que determine o salário atual desse funcionário.
    Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

""")
def calcula_aumento(salario, aumento):
    return salario + (salario * (aumento / 100))

salario_inicial = 1000
aumento = 1.5
ano = 1995
salario_atual = 0

salario_atual = calcula_aumento(salario_inicial, aumento)
ano += 1

while ano < date.today().year:
    ano += 1
    aumento = aumento * 2
    salario_atual = calcula_aumento(salario_atual, aumento)

print(f"O salário atual do funcionário é: R$ {salario_atual:.2f}")

while True:
    salario_inicial = float(input("Digite o salário do próximo funcionário: "))

    aumento = 1.5
    ano = 1995
    salario_atual = calcula_aumento(salario_inicial, aumento)
    ano += 1

    while ano < date.today().year:
        ano += 1
        aumento = aumento * 2
        salario_atual = calcula_aumento(salario_atual, aumento)

    print(f"O salário atual do funcionário é: R$ {salario_atual:.2f}")