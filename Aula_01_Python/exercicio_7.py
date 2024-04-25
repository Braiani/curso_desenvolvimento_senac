def preco_por_cor(cor):
    valores = [
        ["Azul", 20.0],
        ["Laranja", 30.0],
        ["Roxo", 40.0],
        ["Marrom", 50.0]
    ]
    for cor_array in valores:
        if cor_array[0] == cor:
            return cor_array[1]
        
    return False

cor_digitada = input("Digite a cor da etiqueta: ").capitalize()

if preco_por_cor(cor_digitada):
    print(f"O valor do produto pesquisado é R$ {preco_por_cor(cor_digitada)}")
else:
    print("Valor não localizado!")