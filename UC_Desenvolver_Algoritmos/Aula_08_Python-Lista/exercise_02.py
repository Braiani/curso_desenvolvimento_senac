print("""
Enunciado do exercício:
      2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
      mostrando uma mensagem de erro e voltando a pedir as informações.
""")

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while usuario == senha:
    print("Dados inválidos!")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

print("Bem vindo!")