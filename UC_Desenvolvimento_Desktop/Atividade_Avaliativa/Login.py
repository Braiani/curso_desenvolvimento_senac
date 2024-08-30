import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from Usuarios import Usuarios
from SqlHandler import SqlHandler
import os

# from Application import Application

class Application:
    def __init__(self, janela: ctk.CTk):
        SqlHandler()
        self.janela = janela
        self.images = []
        self.buttons = []
        self.background = 'gray'
        self.title = 'Restaurante do Ederson'

    def set_geometry(self, width, height, center = True, fullscreen = False):
        try:
            os_type = os.uname().sysname
        except:
            os_type = 'Windows'
        if fullscreen:
            if os_type == 'Linux':
                self.janela.attributes('-zoomed', True)
            else:
                self.janela.state('zoomed')
            return
        
        if center:
            screen_width = self.janela.winfo_screenwidth()
            screen_height = self.janela.winfo_screenheight()

            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            self.janela.geometry(f"{width}x{height}+{x}+{y}")
        else:
            self.janela.geometry(f"{width}x{height}")

    def set_title(self, title=""):
        self.janela.title(title)

    def set_background(self, color):
        self.background = color
        self.janela.config(background=color)

    def adicionar_entry(self, relx, rely, options: dict = {}):
        entrada = ctk.CTkEntry(self.janela)
        if options:
            for key, value in options.items():
                entrada[key] = value
        entrada.pack(padx=relx, pady=rely)

    def adicionar_label(self, text, relx, rely, options: dict = {}):
        label = ctk.CTkLabel(self.janela, text=text)
        if options:
            for key, value in options.items():
                label[key] = value
        label.pack(padx=relx, pady=rely)

    def adicionar_button(self, text, relx, rely, command, options: dict = {}):
        btn = ctk.CTkButton(self.janela, text=text, command=command, 
                            fg_color="#d4f7b2",
                            hover_color="#81c93c")
        if options:
            for key, value in options.items():
                btn[key] = value
        btn.pack(padx=relx, pady=rely)

        self.buttons.append(btn)

    def start(self):
        self.janela.mainloop()

class Login(Application):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(400, 400, True)
        self.set_title('Login')
        # self.set_background('gray')
        self.entradas = []
        self.logado = False
        self.usuario = None

        self.adicionar_label(text='Usuário', relx=10, rely=10)
        self.adicionar_entry(relx=10, rely=10)
        self.adicionar_label(text='Senha', relx=10, rely=10)
        self.adicionar_entry(relx=10, rely=10, options={'show': '*'})
        self.adicionar_label(text='Confirmar Senha', relx=10, rely=10)
        self.adicionar_entry(relx=10, rely=10, options={'show': '*'})
        self.adicionar_button(text='Entrar', relx=10, rely=10,command=lambda: self.validar_login())

    def get_logado(self):
        if self.logado:
            return self.usuario
        
        return False

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
            self.logado = True
            self.usuario = result[0][1]
            return

        messagebox.showerror('Erro', 'Credenciais inválidas!')

if __name__ == '__main__':
    root = ctk.CTk()
    app = Login(root)
    app.start()