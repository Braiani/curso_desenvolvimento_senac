try:
    sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
    
    if sexo > 2 or sexo < 1: raise ValueError("Sexo Inválido")

    peso = float(input("Digite o seu peso (use . para separar decimal): "))
    altura = int(input("Digite a sua altura em centimetros: "))
    idade = int(input("Digite a sua idade em anos: "))

    if sexo == 1:
        resut = 66.47 + (13.75 * peso) + (5.003 * altura) - (6.775 * idade)
    else:
        resut = 655.09 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade)
    
    print(f"Seu gasto basal é de {resut:.2f}")
except ValueError as e:
    print(f"Erro: {e}")