print("""
Enunciado do exercício:
    Crie um programa que gera os primeiros 'n' números da sequência de Fibonacci. A sequência começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.
""")

def fibonnacci(steps):
    sequencia = [0,1]
    if steps <= 2:
        return sequencia
    
    for i in range(2, steps):
        soma = sequencia[i-1] + sequencia[i-2]
        sequencia.append(soma)
    
    return sequencia
    
num = int(input("Digite quantos números da sequência de Fibonnacci deseja ver: "))

if num < 3:
    print("O mínimo de elementos são 2!")

sequencia = fibonnacci(num)

print(f"Sequência de Fibo: {sequencia}")