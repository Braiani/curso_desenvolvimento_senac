print("""
Enunciado do exercício:
    15. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares
""")

numeros = []
num_pars = []
num_impars = []

for i in range(10):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            break
        except:
            print("Valor inválido")
        
    numeros.append(num)
    if num % 2:
        num_impars.append(num)
    else:
        num_pars.append(num)

print(f"Foram digitados {len(num_pars)} números pares - Somados dá {sum(num_pars)}")
print(f"Foram digitados {len(num_impars)} números ímpares - Somados dá {sum(num_impars)}")