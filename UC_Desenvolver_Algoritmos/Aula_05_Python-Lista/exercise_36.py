print("""
Enunciado do exercício:
    36. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo de serviço de cada funcionário.
      Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior,
      e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Crie um programa que leia:
        • o valor do salário atual do funcionário;
        • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
""")

salario_atual = float(input("Digite o seu salário atual: "))
tempo_servico = float(input("Digite o seu tempo de serviço: "))

salario_novo = salario_atual
reajuste = 1
bonus = 0

if tempo_servico >= 1 and tempo_servico <= 3:
    bonus = 100
elif tempo_servico > 3 and tempo_servico <= 6:
    bonus = 200
elif tempo_servico > 6 and tempo_servico <= 10:
    bonus = 300
elif tempo_servico > 10:
    bonus = 500

if salario_atual <= 500:
    reajuste = 1.25
elif salario_atual <= 100:
    reajuste = 1.2
elif salario_atual <= 1500:
    reajuste = 1.15
elif salario_atual <= 2000:
    reajuste = 1.1

salario_novo = (salario_atual * reajuste) + bonus

print(f"O novo salário do funcionário será: R$ {salario_novo:.2f}")