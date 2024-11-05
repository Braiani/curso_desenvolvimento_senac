from Usuario import Usuario
from Livro import Livro
from Biblioteca import Biblioteca
from Controllers.Livro import ControllerLivro

def print_menu():
    print("""
1 - Pesquisar Livro
2 - Emprestar Livro
3 - Devolver Livro
5 - Sair
""")
    
print("Seja bem-vindo a NOSSA Biblioteca!")

usuario = input("Digite seu usuario: ")
senha = input("Digite seu senha: ")
login = False

