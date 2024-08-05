print("""
Enunciado do exercício:
    5. Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:
        F - Feminino, M - Masculino ou Sexo Inválido.
""")

sexo = input("Digite o sexo da pessoa (F/M): ").capitalize()

if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")