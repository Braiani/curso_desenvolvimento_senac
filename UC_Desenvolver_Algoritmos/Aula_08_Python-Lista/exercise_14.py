print("""
Enunciado do exercício:
    14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a 
    função de potência da linguagem.
""")

while True:
    try:
        base = float(input("Digite a base da potenciação: "))
        expoente = float(input("Digite o expoente da potenciação: "))
        break
    except:
        print("Valores inválidos")

print(f"O resultado de {base} elevado a {expoente} é {base ** expoente}")