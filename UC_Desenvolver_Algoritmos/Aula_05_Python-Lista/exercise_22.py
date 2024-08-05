print("""
Enunciado do exercício:
    22. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
      Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.
""")
dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

dia = int(input("Digite um número de 1 a 7: "))

if dia > 7 or dia < 1:
    print("Número inválido")
else:
    print(f"O dia da semana digitado foi {dias_semana[dia - 1]}")