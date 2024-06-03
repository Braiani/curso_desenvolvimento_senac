nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade < 0:
    print(f"Olá, {nome}, você ainda não nasceu.")
else:
    print(f"Olá, {nome}, você tem {idade} anos.")