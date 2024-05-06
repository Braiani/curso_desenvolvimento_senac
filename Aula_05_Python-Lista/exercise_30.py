print("""
Enunciado do exercício:
    30. Uma empresa vende o mesmo produto para quatro diferentes estados.
      Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
      Crie um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto
      acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
""")

estado = input("Digite o Estado de destino: ").upper()

if estado != "MG" and estado != "SP" and estado != "RJ" and estado != "MS":
    print("Estado digitado inválido!")
    exit()

valor = float(input("Digite o valor da venda: "))

imposto_percentual = 0

if estado == "MG":
    imposto_percentual = 7
elif estado == "SP":
    imposto_percentual = 12
elif estado == "RJ":
    imposto_percentual = 15
else:
    imposto_percentual = 8

total = valor + (valor * (imposto_percentual / 100))

print(f"O valor total para envio do produto para {estado} é R$ {total:.2f}")