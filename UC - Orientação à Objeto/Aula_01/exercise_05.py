print("""
Enunciado do exercício:
    Programe um software que recebe três números e cria duas funções: uma que retorna o maior número e outra que retorna o menor número.
""")

def maior_numero(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3
    return num1

def menor_numero(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        return num1
    if num2 < num1 and num2 < num3:
        return num2
    if num3 < num1 and num3 < num2:
        return num3
    return num1

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

print(f"O maior número é: {maior_numero(num1,num2,num3)}")
print(f"O menor número é: {menor_numero(num1,num2,num3)}")