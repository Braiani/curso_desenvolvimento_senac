print("""
Enunciado do exercício:
    9. Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas com os valores invertidos.
""")

numero1 = float(input("Digite o 1º número que deseja inverter: "))
numero2 = float(input("Digite o 2º número que deseja inverter: "))

temp = numero1
numero1 = numero2
numero2 = temp

print(f"O inverso do 1º seu número é: {numero1}")
print(f"O inverso do 2º seu número é: {numero2}")