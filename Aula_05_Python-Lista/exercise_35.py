print("""
Enunciado do exercício:
    35. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
""")

venda = float(input("Qual o valor da venda? "))

if venda < 20000:
    comissao = 400 * 1.14
elif venda < 40000:
    comissao = 500 * 1.14
elif venda < 60000:
    comissao = 550 * 1.14
elif venda < 80000:
    comissao = 600 * 1.14
elif venda < 100000:
    comissao = 650 * 1.14
else:
    comissao = 700 * 1.16


print("O valor da comissão é R$", "{:.2f}".format(comissao).replace(".", ","))