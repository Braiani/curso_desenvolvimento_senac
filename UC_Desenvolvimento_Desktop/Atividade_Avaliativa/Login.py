from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Usuarios import Usuarios

from Application import Application

class Login(Application):
    def __init__(self):
        super().__init__()
        self.set_geometry(400, 300, True)
        self.set_title('Login')
        self.set_background('gray')
        self.entradas = []

        self.adicionar_label('Usuário', 0.5, 0.2, CENTER)
        self.adicionar_entry(0.5, 0.3, CENTER, {'width': 20})
        self.adicionar_label('Senha', 0.5, 0.4, CENTER)
        self.adicionar_entry(0.5, 0.5, CENTER, {'width': 20, 'show': '*'})
        self.adicionar_label('Confirmar Senha', 0.5, 0.6, CENTER)
        self.adicionar_entry(0.5, 0.7, CENTER, {'width': 20, 'show': '*'})
        self.adicionar_button('Entrar', 0.5, 0.8, CENTER, lambda: self.validar_login())

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
        
        if senha != confirmar_senha:
            messagebox.showerror('Erro', 'Senhas não coincidem!')
            return

        usuarios = Usuarios(usuario, senha)
        result = usuarios.validar_login()

        if result:
            messagebox.showinfo('Sucesso', "Login Realizado com sucesso!")
            self.janela.destroy()
            return

        messagebox.showerror('Erro', 'Credenciais inválidas!')