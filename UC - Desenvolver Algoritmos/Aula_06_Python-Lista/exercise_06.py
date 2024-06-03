print("""
Enunciado do exercício:
    6 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
      Faça um programa que implemente uma caixa registradora rudimentar.
      O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
      Um valor zero deve ser informado pelo operador para indicar o final da compra.
      O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
      Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
      A saída deve ser conforme o exemplo abaixo:
      
      Lojas Tabajara 
        Produto 1: R$ 2.20 
        Produto 2: R$ 5.80 
        Produto 3: R$ 1.00 
        Total: R$ 9.00 
        Dinheiro: R$ 20.00 
        Troco: R$ 11.00
""")

while True:
  produtos = []
  total = 0
  recebido = 0
  troco = 0
  i = 0

  print("Bem vindo a Lojas Tabajara")

  while True:
    valor = float(input(f"Digite o valor do produto {i + 1}: "))
    if valor == 0:
      break

    i += 1
    produtos.append(valor)
    total += valor
  
  print(f"O total dos produtos é R$ {total:.2f}")

  while recebido < total:
    recebido += float(input("Digite o valor recebido do cliente: "))
    print(f"Valor total recebido R$ {recebido:.2f}")
    if recebido >= total:
      break
  
  if recebido > total:
    troco = recebido - total
  
  j = 0
  print("\nLojas Tabajara")
  while j < len(produtos):
    print(f"Produto {j + 1}: R$ {produtos[j]:.2f}")
    j += 1
  print(f"Total: R$ {total:.2f}")
  print(f"Recebido: R$ {recebido:.2f}")
  print(f"Troco: R$ {troco:.2f}")

  print("----------------------------------------------------------", end="\n\n\n")