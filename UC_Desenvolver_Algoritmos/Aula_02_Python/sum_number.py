soma = 0
i = 0

while True:
    i += 1
    valor = float(input(f"Digite o {i}º número: "))
    if valor == 0:
        break
    soma += valor


print(f"Você digitou {i} números e a soma dos números digitados foi: {soma}")