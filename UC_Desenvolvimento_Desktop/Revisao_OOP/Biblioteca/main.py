from Usuario import Usuario
from Livro import Livro

def print_menu():
    print("""
1 - Pesquisar Livro
2 - Emprestar Livro
3 - Devolver Livro
5 - Sair
""")
    
print("Seja bem-vindo a NOSSA Biblioteca!")

usuarios = [
    Usuario('admin', 'pass', 'Administrador'),
    Usuario('user', 'password', 'Usuário'),
    Usuario('leitor', '123', 'Leitor'),
]

usuario = input("Digite seu usuario: ")
senha = input("Digite seu senha: ")
login = False

for user in usuarios:
    if user.valida_login(usuario, senha):
        login = user
        break

if not login:
    exit()

livros = [
    Livro().cadastrar('Harry Potter', 'Harry Davidson', '123456789'),
    Livro().cadastrar('Fenix Voadora', 'Davidson Harry', '223456789'),
    Livro().cadastrar('Pedra Filosofal', 'Har Don', '323456789'),
]


while True:
    print_menu()
    escolha = int(input("Digite sua opção: "))

    if escolha == 5:
        break
    if escolha == 1:
        titulo = input("Digite o título que deseja buscar: ")
        for livro in livros:
            if livro.titulo == titulo:
                print("Livro encontrado! Deseja realizar o empréstimo? (S/N)")
                if input().lower() == 's':
                    if livro.pode_emprestar() and login.pode_emprestar():
                        pass
                
                break