print("""
Enunciado do exercício:
    25. Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
      O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.
""")

conta = input("Digite a conta que quer fazer: ")

print(f"O resultado da conta é {eval(conta)}")