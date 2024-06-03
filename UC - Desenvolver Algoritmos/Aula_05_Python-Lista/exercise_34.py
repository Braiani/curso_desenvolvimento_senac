print("""
Enunciado do exercício:
    34. Um produto vai sofrer aumento de acordo com a tabela abaixo.
      Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).
""")

preco_anterior = float(input("Qual o preço antigo? "))

if preco_anterior <= 50:
    novo_preco = preco_anterior * 1.05
    print(f"Novo preço com reajuste de 5%: R$ {novo_preco:.2f}")

elif preco_anterior <= 100:
    novo_preco = preco_anterior * 1.1
    print(f"Novo preço com reajuste de 10%: R$ {novo_preco:.2f}")

else:
    novo_preco = preco_anterior * 1.15
    print(f"Novo preço com reajuste de 15%: R$ {novo_preco:.2f}")