class Login:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
    
    def logar(self):
        if self.user != 'admin':
            raise Exception
        if self.password != '123':
            raise Exception
        return True

if __name__ == "__main__":
    try:
        usuario = input("Digite seu usuário: ")
        senha = int(input("Digite sua senha: "))

        login = Login(usuario, senha)
        if login.logar():
            print("Usuário autenticado!")
    except:
        print("Ocorreu um erro!")