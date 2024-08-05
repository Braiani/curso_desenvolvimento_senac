print("""
Enunciado do exercício:
    37. O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
      A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
      Leia o custo de fábrica e escreva o custo ao consumidor.
""")

custo_carro = int(input("Digite o valor do custo de fábrica do carro: "))

distribuidor = 0
imposto = 1

if custo_carro < 12000:
    distribuidor = 1.05
elif custo_carro >= 12000 and custo_carro < 25000:
    distribuidor = 1.1
    imposto = 1.15
else:
    distribuidor = 1.15
    imposto = 1.2

valor_final = (custo_carro * distribuidor) + (custo_carro * imposto)

print(f"O valor final do carro é R$ {valor_final:.2f}")