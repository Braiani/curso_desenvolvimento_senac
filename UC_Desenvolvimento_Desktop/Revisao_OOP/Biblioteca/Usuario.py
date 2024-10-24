class Usuario:
    MAX_EMPRESTIMO = 5

    def __init__(self, login, senha, nome) -> None:
        self.login = login
        self.senha = senha
        self.nome = nome
        self.livros = []
    
    
    def pode_emprestar(self):
        return len(self.livros) < self.MAX_EMPRESTIMO
    
    def emprestar(self, livro):
        if not self.pode_emprestar:
            print("Usuário não pode realizar empréstimo!")
            return
        
        self.livros.append(livro)

    def valida_login(self, login, senha):
        if login == self.login and senha == self.senha:
            print(f"Seja bem-vindo {self.nome}!")
            return True
        
        return False