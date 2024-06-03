print("""
Enunciado do exercício:
    40. Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
      Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
      8% para o INSS e 5% para o sindicato, Crie um programa que nos dê:
        - salário bruto.
        - quanto pagou ao INSS.
        - quanto pagou ao sindicato.
        - o salário líquido.
""")

horas_trabalhadas = float(input("Digite quantas horas você trabalha por mês: "))
valor_hora = float(input("Digite quanto você ganha por hora: "))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)


print(f"""
- Salário Bruto (R$): {salario_bruto:.2f}
- Imposto de Rendas (R$): {imposto_renda:.2f}
- INSS (R$): {inss:.2f}
- Sindicato (R$): {sindicato:.2f}
- Salário Líquido (R$): {salario_liquido:.2f}
""")