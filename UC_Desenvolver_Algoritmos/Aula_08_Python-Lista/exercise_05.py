print("""
Enunciado do exercício:
    5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
""")

while True:
    paisA = int(input("Digite a população do País A: "))
    paisB = int(input("Digite a população do País B: "))
    i = 0

    if paisA >= paisB or paisA < 0 or paisB < 0:
        print("Dados inválidos! Tente novamente!")
        continue

    while paisA <= paisB:
        paisA *= 1.03
        paisB *= 1.015
        i += 1
        
    print(f"Demorará {i} anos")

    sair = int(input("Digite 0 para sair: "))
    if sair == 0:
        break