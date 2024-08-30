import customtkinter as ctk
from tkinter import messagebox
from Usuarios import Usuarios
from Application import Application

class Login(Application):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(400, 400, True)
        self.set_title('Login')
        self.entradas = []
        self.logado = False
        self.usuario = None
        self.set_itens_screen()

    def set_itens_screen(self):
        self.adicionar_label(text='Usuário', padx=0, pady=0)
        usuario = self.adicionar_entry(padx=0, pady=0)
        usuario.configure(placeholder_text="Usuário")
        self.entradas.append(usuario)

        self.adicionar_label(text='Senha', padx=0, pady=0)
        senha = self.adicionar_entry(padx=0, pady=0)
        senha.configure(placeholder_text="Senha")
        senha.configure(show="*")
        self.entradas.append(senha)

        self.adicionar_label(text='Confirmar Senha', padx=0, pady=0)
        conf_senha = self.adicionar_entry(padx=0, pady=0)
        conf_senha.configure(placeholder_text="Confirmar Senha")
        conf_senha.configure(show="*")
        self.entradas.append(conf_senha)

        self.adicionar_button(text='Entrar', padx=0, pady=25,command=lambda: self.validar_login())

    def get_logado(self):
        if self.logado:
            return self.usuario
        
        return False

    def validar_login(self):
        usuario = self.entradas[0].get()
        senha = self.entradas[1].get()
        confirmar_senha = self.entradas[2].get()

        if not usuario or not senha:
            messagebox.showerror('Erro', 'Usuário e senha são obrigatórios')
            return
        
        if usuario == senha:
            messagebox.showerror('Erro', 'Usuário e senha não podem coincidir')
            return
        
        if senha != confirmar_senha:
            messagebox.showerror('Erro', 'Senhas não coincidem!')
            return

        usuarios = Usuarios(usuario, senha, self.connector)
        result = usuarios.validar_login()

        if result:
            messagebox.showinfo('Sucesso', "Login Realizado com sucesso!")
            self.janela.destroy()
            self.logado = True
            self.usuario = result[0][1]
            return

        messagebox.showerror('Erro', 'Credenciais inválidas!')

if __name__ == '__main__':
    root = ctk.CTk()
    app = Login(root)
    app.start()