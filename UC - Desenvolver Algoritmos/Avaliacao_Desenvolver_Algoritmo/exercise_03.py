print("""
Enunciado do exercício:
    3 - A média harmônica amortizada é definida segundo uma fórmula matemática, onde N é o número de notas a serem usadas na média, ni é a i-ésima nota,
    e X é o fator de amortização. Implemente um algoritmo em Python que calcule a média de 3 notas de um aluno
    digitadas no teclado, com fator de amortização igual a 4. Em seguida, informe se o aluno passou (média >= 5) ou não (média < 5).
""")

n = [0,0,0]
amortizacao = 4
media_harmonica = 0
n_elementos = len(n)

n[0] = float(input("Digite a 1ª nota: "))
n[1] = float(input("Digite a 2ª nota: "))
n[2] = float(input("Digite a 3ª nota: "))

somatorio = 0
for elemento in n:
    somatorio += 1 / (elemento + amortizacao)

media_harmonica = (n_elementos / somatorio) - amortizacao

if media_harmonica >= 5:
    print(f"Você passou, sua média é {media_harmonica:.1f}")
else:
    print(f"Você não passou, sua média é {media_harmonica:.1f}")