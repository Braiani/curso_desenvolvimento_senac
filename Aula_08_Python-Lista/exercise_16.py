print("""
Enunciado do exercício:
    16. A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.
""")

n_esimo = int(input("Digite o termo final do Fibonacci: "))

fibonacci = [1, 1]

while len(fibonacci) < n_esimo:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

print(f"A sequência de Fibonacci de {n_esimo} elementos é: {str(fibonacci).replace('[', '').replace(']', '')}")