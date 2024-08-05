print("""
Enunciado do exercício:
    39. Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
      Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
      que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
      Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
        - comprar apenas latas de 18 litros;
        - comprar apenas galões de 3,6 litros;
""")

area_pintura = float(input("Digite a área a ser pintada (em m²): "))

litros_necessarios = area_pintura / 6

latas = litros_necessarios // 18
galoes = litros_necessarios // 3.6

if litros_necessarios % 18:
    latas += 1
if litros_necessarios % 3.6:
    galoes +=1

print("Para suas necessidades, temos as seguintes opções: ")
print(f"Comprar apenas latas de 18 litros: R$ {latas * 80:.2f} - {latas:.0f} latas")
print(f"Comprar apenas galões de 3,6 litros: R$ {galoes * 25:.2f} - {galoes:.0f} galões")