print("""
Enunciado do exercício:
    16. Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários acima de R$ 2500,00.
      Dado o número de horas trabalhadas por um funcionário, informar o valor do seu salário líquido.
""")

horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
imposto = 11 / 100
salario = 0
salario_liquido = 0
VALOR_HORA = 40.5

salario = horas * VALOR_HORA

if salario > 2500:
    salario_liquido = salario - (salario * imposto)
else:
    salario_liquido = salario

print(f"O salario líquido do funcionaário é R$ {salario_liquido:.2f}")