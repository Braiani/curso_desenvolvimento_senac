print("""
Enunciado do exercício:
    Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A fórmula de conversão é: F=9/5C+32
""")

def converte_c_para_f(temperatura):
    return ((9/5) * temperatura) + 32

celsius = float(input("Digite a temperatura em Celsius: "))

print(f"A temperatura de {celsius} ºC em Fahrenheit é {converte_c_para_f(celsius)}")