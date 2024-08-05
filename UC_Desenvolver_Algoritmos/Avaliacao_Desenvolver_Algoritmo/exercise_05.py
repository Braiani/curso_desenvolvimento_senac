print("""
Enunciado do exercício:
    5 - Num país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar os seu impostos porque sabem que não existem
    políticos corruptos e que os impostos são usados para beneficiar a população, sem qualquer apropriação indevida.
    A moeda deste país é o Rombus (R$). Leia um valor com 2 dígitos após a vírgula, equivalente ao salário de um habitante do Lisarb.
    Em seguida, imprima o valor devido que essa pessoa deverá pagar de impostos, conforme tabela abaixo:
      +======================+=========+
      |  Salário             | Taxa    |
      +======================+=========+
      |  0.00 a 2.000,00     | Isento  | 
      |  2.000.01 a 3.000,00 | 8%      |
      |  3.000,01 a 4.500,00 | 18%     |
      |  Acima de 4.500,00   | 28%     |
      +======================+=========+
""")

salario = float(input("Digite o salário (apenas dois números após o ponto): "))


if salario <= 2000:
    print("Isento")
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08

    print(f"R$ {imposto:.2f}")
elif salario <= 4500:
    imposto = 1000 * 0.08
    imposto += (salario - 3000) * 0.18

    print(f"R$ {imposto:.2f}")
else:
    imposto = 1000 * 0.08
    imposto += 1500 * 0.18
    imposto += (salario - 4500) * 0.28

    print(f"R$ {imposto:.2f}")