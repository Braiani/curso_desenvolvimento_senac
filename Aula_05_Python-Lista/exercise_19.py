print("""
Enunciado do exercício:
    19. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
      Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
      Se o número lido não for maior do que zero, o programa termina com a mensagem “Número inválido”.
""")

numeros = input("Digite um valor: ")

soma = 0

if numeros[0] == "-":
    print("Número inválido")
    exit()

# i = 0
# while i < len(numeros):
#     soma += int(numeros[i])
#     i += 1

for numero in numeros:
    print(numero)
    soma += int(numero)

print(f"Soma total: {soma}")