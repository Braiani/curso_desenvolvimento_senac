i = 0
num_max = 15
texto_final = ''

while i < num_max:
    number = int(input("Digite um número inteiro: "))
    i += 1
    if not number % 2:
        if texto_final == "":
            texto_final = str(number)
        else:
            texto_final = texto_final + ", " + str(number)

print("Os números pares digitados foram: ")
print(texto_final)