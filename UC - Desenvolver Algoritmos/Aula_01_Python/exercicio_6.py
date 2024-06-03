conta = input("Digite a conta que deseja fazer (sem espaços): ")
numeros = []
while "+" in conta or "-" in conta:
    if "+" in conta:
        numeros.append(conta.split("+"))
        print(numeros)
        break
        # resultado = int(numeros[0]) + int(numeros[1])
        # print(f"O resultado da conta é {resultado}")
    elif "-" in conta:
        numeros = conta.split("-")
        print(numeros)
        # resultado = int(numeros[0]) - int(numeros[1])
        # print(f"O resultado da conta é {resultado}")
    else:
        print("Operação inválida!")

print(numeros)