print("""
Enunciado do exercício:
    20. Crie um algoritmo que calcule a média ponderada das notas de 3 provas.
      A primeira e a segunda prova têm peso 1 e a terceira tem peso 2.
      Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
      A nota para aprovação deve ser igual ou superior a 60 pontos.
""")

nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))
nota3 = float(input("Digite a 3ª nota do aluno: "))

media = (nota1 + nota2 + (nota3 * 2)) / 4

if media >= 60:
    print(f"Aluno Aprovado com nota: {media}")
else:
    print(f"Aluno Reprovado com nota: {media}")