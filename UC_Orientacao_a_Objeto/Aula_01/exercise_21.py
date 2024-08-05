print("""
Enunciado do exercício:
    Implemente um programa que verifica se um número de CPF é válido. O CPF é composto por 11 dígitos e possui um algoritmo de validação específico.
""")

def calcula_primeiro_dv(cpf):
    soma = 0
    j = 0
    for i in range(10, 1, -1):
        soma += i * int(cpf[j])
        j += 1
    return (soma * 10) % 11

def calcula_segundo_dv(cpf):
    soma = 0
    j = 0
    for i in range(11, 1, -1):
        soma += i * int(cpf[j])
        j += 1
    return (soma * 10) % 11

def valida_cpf(cpf):
    if len(cpf) < 11 or len(cpf) > 11:
        return False
    if calcula_primeiro_dv(cpf) != int(cpf[9]):
        return False
    if calcula_segundo_dv(cpf) != int(cpf[10]):
        return False
    return True
    

cpf = input("Digite seu CPF (apenas números): ")

if valida_cpf(cpf):
    print("CPF Válido")
else:
    print("CPF Inválido")