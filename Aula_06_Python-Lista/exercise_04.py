print("""
Enunciado do exercício:
      4 - Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e
      que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
      Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
      mantidas as taxas de crescimento.
""")

paisA = 80000
paisB = 200000
i = 0

while paisA <= paisB:
    paisA *= 1.03
    paisB *= 1.015
    i += 1

print(f"Demorará {i} anos")