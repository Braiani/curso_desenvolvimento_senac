print("""
Enunciado do exercício:
    15. Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
      Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
      este fato deve será informado ao usuário e o programa termina.
""")
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
    print("Notas digitadas inválidas!")
    exit()

media = (nota1 + nota2) / 2

print(f"A média do aluno é {media}")