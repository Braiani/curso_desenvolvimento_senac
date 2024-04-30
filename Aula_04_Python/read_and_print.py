soma_numeros_positivo = 0
numeros_negativos = 0
i = 0

while i < 20:
    number = int(input(f"Digite o {i+1}º número: "))
    if number == 0:
        print("Número inválido! Digite um número diferente de 0.")
        continue
    if number > 0:
        soma_numeros_positivo += number
    elif number < 0:
        numeros_negativos += 1
    i += 1

print(f"A soma dos números positivos é: {soma_numeros_positivo}")
print(f"A quantidade de números negativos é: {numeros_negativos}")
