print("""
Enunciado do exercício:
      1 - Faça um programa que peça uma nota, entre zero e dez.
      Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
""")

while True:
    nota = float(input("Digite uma nota: "))

    if nota >= 0 and nota <= 10:
        print("Nota válida!")
        break
    
    print("Nota inválida!")