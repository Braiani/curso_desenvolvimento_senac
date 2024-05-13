print("""
Enunciado do exercício:
    3. Faça um programa que leia e valide as seguintes informações: 
        a. Nome: maior que 3 caracteres; 
        b. Idade: entre 0 e 150; 
        c. Salário: maior que zero; 
        d. Sexo: 'f' ou 'm'; 
        e. Estado Civil: 's', 'c', 'v', 'd'; 
    Use a função len(string) para saber o tamanho de um texto (número de caracteres).
""")

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("O nome deve ter mais que 3 caracteres!")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("A idade deve ser entre 0 e 150")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario < 0:
    print("O seu salário deve ser maior que zero")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (f, m ou o): ")
while sexo.lower() != "m" and sexo.lower() != "f" and sexo.lower() != "o":
    print("sexo digitado inválido!")
    sexo = input("Digite seu sexo (f, m ou o): ")

estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ")
while estado_civil.lower() != "s" and estado_civil.lower() != "c" and estado_civil.lower() != "v" and estado_civil.lower() != "d":
    print("Estado civil digitado inválido!")
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ")

print("Cadastro realizado com sucesso!!!")