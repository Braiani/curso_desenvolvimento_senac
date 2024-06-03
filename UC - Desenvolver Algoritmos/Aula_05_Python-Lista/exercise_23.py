print("""
Enunciado do exercício:
    23. Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número.
      Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.
""")
meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Digite um número de 1 a 12: "))

if mes >= 1 and mes <= 12:
    print(f"O mês digitado foi {meses_ano[mes - 1]}")
else:
    print("Número inválido")