print("""
Enunciado do exercício:
    6. Crie um Programa que pergunte em que turno você estuda.
      Peça para digitar M - Matutino ou V- Vespertino ou N - Noturno.
      Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
""")

print("""
Para a próxima pergunta, utilize as seguintes opções:
M - Matutino
V- Vespertino
N - Noturno
""")
turno = input("Digite o turno que você estuda: ").capitalize()

if turno == "M":
    print("M - Matutino")
elif turno == "V":
    print("V- Vespertino")
elif turno == "N":
    print("N - Noturno")
else:
    print("Valor Inválido")