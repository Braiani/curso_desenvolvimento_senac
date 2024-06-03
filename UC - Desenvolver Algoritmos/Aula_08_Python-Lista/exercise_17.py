print("""
Enunciado do exercício:
    17. A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
""")

fibonacci = [0, 1]

while True:
    proximo = fibonacci[-1] + fibonacci[-2]
    if proximo > 500:
        break
    fibonacci.append(proximo)

print(f"A sequência de Fibonacci é: {str(fibonacci).replace('[', '').replace(']', '')}")
