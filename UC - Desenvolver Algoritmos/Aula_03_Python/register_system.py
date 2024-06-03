name = ''
age = 0
salary = 0
sex = ''

name = input("Digite seu nome: ")
while len(name) <= 3:
    print("O nome deve ter mais que 3 caracteres!")
    name = input("Digite seu nome: ")

age = int(input("Digite sua idade: "))
while age < 0 or age > 150:
    print("A idade deve ser entre 0 e 150")
    age = int(input("Digite sua idade: "))

salary = float(input("Digite seu salário: "))
while salary < 0:
    print("O seu salário deve ser maior que zero")
    salary = float(input("Digite seu salário: "))

sex = input("Digite seu sexo (M/F): ")
while sex.upper() != "M" and sex.upper() != "F":
    print("Sexo digitado inválido!")
    sex = input("Digite seu sexo (M/F): ")

print("Cadastro realizado com sucesso!!!")