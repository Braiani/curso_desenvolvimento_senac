from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
from Usuarios import Usuarios
from Application import Application


class Login(Application):
    def __init__(self):
        super().__init__()
        self.set_geometry(400, 300, False)
        self.set_title('Login')
        self.set_background('gray')
        self.entradas = []

        self.adicionar_label('Usuário', 0.5, 0.2, CENTER)
        self.adicionar_entry(0.5, 0.3, CENTER, {'width': 20})
        self.adicionar_label('Senha', 0.5, 0.4, CENTER)
        self.adicionar_entry(0.5, 0.5, CENTER, {'width': 20, 'show': '*'})
        self.adicionar_label('Confirmar Senha', 0.5, 0.6, CENTER)
        self.adicionar_entry(0.5, 0.7, CENTER, {'width': 20, 'show': '*'})
        self.adicionar_button('Entrar', 0.5, 0.8, CENTER, self.validar_login)

    def adicionar_entry(self, relx, rely, anchor, options: dict = {}):
        entrada = ttk.Entry(self.janela)
        self.entradas.append(entrada)
        if options:
            for key, value in options.items():
                entrada[key] = value
        entrada.place(relx=relx, rely=rely, anchor=anchor)

    def validar_login(self):
        usuario = self.entradas[0].get()
        senha = self.entradas[1].get()
        confirmar_senha = self.entradas[2].get()

        if usuario == senha:
            messagebox.showerror('Erro', 'Usuário e senha não podem coincidir')
            return

        if not usuario or not senha:
            messagebox.showerror('Erro', 'Usuário e senha são obrigatórios')
            return

        usuarios = Usuarios(usuario, senha, confirmar_senha)
        result = usuarios.validar_login()

        if result['code'] == 200:
            messagebox.showinfo('Sucesso', result['message'])
            self.janela.destroy()
            return

        messagebox.showerror('Erro', result['message'])


class Main(Application):
    def __init__(self):
        super().__init__()
        self.set_geometry(800, 600)
        self.set_title('Restaurante do Ederson')
        self.set_background('black')

        self.adicionar_label('Restaurante do Ederson', 0.5, 0.1, CENTER, {'font': ('Arial', 20), 'foreground': 'white'})
        self.adicionar_button('Login', 0.5, 0.2, CENTER, self.abrir_login)
        self.adicionar_button('Cadastro', 0.5, 0.3, CENTER, self.abrir_cadastro)

    def abrir_login(self):
        self.janela.destroy()
        login.start()

    def abrir_cadastro(self):
        self.janela.destroy()


def on_closing():
    if messagebox.askokcancel('Sair', 'Deseja realmente sair?'):
        exit()

if __name__ == '__main__':
    try:
        login = Login()
        login.start()
    except Exception as e:
        print(e)
        messagebox.showerror('Erro', 'Ocorreu um erro inesperado!')
        exit()