print("""
Enunciado do exercício:
    31. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
      calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
""")

km_rodado = float(input("Quantos Km foram rodados: "))
litros_consumidos = float(input("Quantos litros de gasosa foram usados: "))

consumo = km_rodado / litros_consumidos

if consumo < 8:
    print("Venda seu carro!")
elif consumo < 12:
    print("Econômico!")
else:
    print("Super Econômico!")