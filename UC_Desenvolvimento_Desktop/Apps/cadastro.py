from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Usuario:

    def __init__(self, usuario, senha, confirmar_senha) -> None:
        self.usuario = usuario
        self.senha = senha
        self.confirmar_senha = confirmar_senha

    def validar_login(self):
        if self.usuario == self.senha:
            return {'code': 403, 'message' :'Usuário e senha não podem coincidir'}
        if self.senha != self.confirmar_senha:
            return {'code': 403, 'message' :'Senhas não coincidem!!'}
        return {'code': 200, 'message' :'Cadastro Realizado com Sucesso!'}

class Programa:
    def __init__(self) -> None:
        self.janela = Tk()
        self.janela.title("Cadastro")
        self.janela.geometry("600x480")
        self.entradas = []

    def adicionar_label(self, text, relx, rely, anchor):
        ttk.Label(self.janela, text=text).place(relx=relx, rely=rely, anchor=anchor)
    
    def adicionar_entry(self, relx, rely, anchor, placeholder = ''):
        entrada = ttk.Entry(self.janela, show=placeholder)
        self.entradas.append(entrada)
        entrada.place(relx=relx, rely=rely, anchor=anchor)

    def adicionar_button(self, text, relx, rely, anchor, command):
        ttk.Button(self.janela, text=text, command=command).place(relx=relx, rely=rely, anchor=anchor)
    
    def get_entradas(self, entrada = None):
        if entrada == None:
            return self.entradas
        return self.entradas[entrada].get()

    def iniciar(self):
        self.janela.mainloop()


def verificar_senha():
    usuario = programa.get_entradas(0)
    senha = programa.get_entradas(1)
    confirm_senha = programa.get_entradas(2)

    if usuario == '' or senha == '' or confirm_senha == '':
        messagebox.showwarning("Validação!", "Campo não preenchido!")
        return

    login = Usuario(usuario, senha, confirm_senha)
    login = login.validar_login()

    if login['code'] == 200:
        messagebox.showinfo('Sucesso', login['message'])
    elif login['code'] == 403:
        messagebox.showerror('Error', login['message'])


if __name__ == '__main__':
    programa = Programa()

    programa.adicionar_label("Digite seu nome", 0.5, 0.20, 'center')
    programa.adicionar_entry(0.5, 0.25, 'center')

    programa.adicionar_label("Digite sua senha", 0.5, 0.30, 'center')
    programa.adicionar_entry(0.5, 0.35, 'center', '*')

    programa.adicionar_label("Confirme sua senha", 0.5, 0.40, 'center')
    programa.adicionar_entry(0.5, 0.45, 'center', '*')

    programa.adicionar_button("Cadastrar", 0.5, 0.6, 'center', verificar_senha)

    programa.iniciar()