print("""
Enunciado do exercício:
    17. Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de acordo com as seguintes condições:
      Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
      Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido,
      caso contrário imprima: Empréstimo concedido.
""")

salario = float(input("Digite o salário: "))
prestacao = float(input("Digite o valor da prestação: "))

MARGEM = 20

if (prestacao / salario) * 100 > 20:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")