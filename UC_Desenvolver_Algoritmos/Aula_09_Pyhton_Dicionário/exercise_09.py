print("""
Enunciado do exercício:
    9. Dicionário de Cores:
      ○ Crie um dicionário com nomes de cores e seus códigos hexadecimais. Peça ao usuário para digitar o nome de uma cor e exiba seu código.
""")

cores = {
    "preto": "#000000",
    "branco": "#FFFFFF",
    "vermelho": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "amarelo": "#FFFF00",
    "roxo": "#800080",
    "laranja": "#FFA500",
    "rosa": "#FFC0CB",
    "cinza": "#808080",
    "marrom": "#A52A2A",
    "azul claro": "#ADD8E6",
    "verde claro": "#90EE90",
    "rosa claro": "#FFB6C1",
    "amarelo claro": "#FFFFE0",
    "roxo claro": "#9370DB",
    "laranja claro": "#FFD700",
    "vermelho escuro": "#8B0000",
    "verde escuro": "#006400",
    "azul escuro": "#00008B"
}

cor = input("Digite a cor que deseja conhecer o hexadecimal: ").lower()

if cor not in cores:
    print()
    print("Cor não existe em nosso banco de dados.")
else:
    print()
    print(f"O valor hexadecimal de {cor} é {cores[cor]}")