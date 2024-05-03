print("""
Enunciado do exercício:
    21. A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente,
      a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
      A média das três notas mencionadas anteriormente obedece aos pesos:
      Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
      De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
      de recuperação (entre 3 e 5,9) ou se foi aprovado. Crie todas as verificações necessárias.
""")

def valida_nota(nota):
    if nota > 0 and nota <= 10:
        return True
    print(f"A Nota {nota} é inválida")
    return False

nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))
nota3 = float(input("Digite a 3ª nota do aluno: "))

if not valida_nota(nota1) or not  valida_nota(nota2) or not valida_nota(nota3):
    print("Dados inválidos!")
    exit()

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

if media > 0 and media < 3:
    print(f"O aluno está reprovado: média {media}")
elif media >= 3 and media < 6:
    print(f"O aluno está de recuperação: média {media}")
else:
    print(f"O aluno foi aprovado: média {media}")