print("""
Enunciado do exercício:
    1 - Faça um script para imprimir uma tabuada utilizando FOR
""")

tabuada = int(input("Digite o número da tabuada que deseja: "))

resultado = []
for num in range(11):
    # print(f"{tabuada} x {num} = {tabuada * num}")
    resultado.append(str(tabuada) +" x " + str(num) + " = " + str(tabuada * num))


for valor in resultado:
    print(valor)