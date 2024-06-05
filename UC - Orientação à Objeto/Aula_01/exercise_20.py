print("""
Enunciado do exercício:
    Faça um programa que calcula o montante final de um investimento com juros compostos. O usuário deve fornecer o capital inicial,
    a taxa de juros anual e o período de investimento em anos.
""")

def calcula_juros_composto(inicial, taxa, tempo):
    taxa = taxa / 100
    montante = inicial * (1 + taxa)**tempo
    return montante - inicial

capital = float(input("Digite seu capital inicial: "))
taxa = float(input("Digite a taxa de juros anual: "))
periodo = int(input("Digite o periodo do seu investimento (em anos): "))

montante = calcula_juros_composto(capital, taxa, periodo)

print(f"O total de juros para o capital de {capital}, em um período de {periodo} anos a uma taxa de {taxa}% ao ano, será: R$ {montante:.2f}")