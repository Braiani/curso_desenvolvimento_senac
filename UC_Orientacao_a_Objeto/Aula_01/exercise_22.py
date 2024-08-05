print("""
Enunciado do exercício:
    Crie um programa que converte um número decimal para binário, octal ou hexadecimal, conforme a escolha do usuário.
""")

def converter_base(numero, base):
    if base == 1:
        return bin(numero)
    elif base == 2:
        return oct(numero)
    else:
        return hex(numero)

num = float(input("Digite o número que deseja converter: "))
print("""
Digite 1 para converter para Binário;
Digite 2 para converter para Octal;
Digite 3 para converter para Hexadecimal;
""")
base = int(input("Digite a base escolhida: "))

if base > 3 or base < 1:
    print("Opção inválida!")
else:
    print(f"O número convertido é: {converter_base(num, base)}")