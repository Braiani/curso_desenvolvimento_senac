from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import *

class BancoDados:
    def __init__(self) -> None:
        pass
    
    def connect(self):
        return True


class Usuario:
    def __init__(self) -> None:
        self.user = ''
        self.senha = ''
        self.banco = BancoDados()
    
    def setar_login_info(self, user, senha):
        self.user = user
        self.senha = senha
        self.logar()
    
    def logar(self):
        try:
            if self.user == '' or self.senha == '':
                raise Exception('Login Inválido!')
            
            if self.banco.connect():
                messagebox.showinfo(title='Login Realizado', message="Login realizado com sucesso!")
        except Exception as error:
            messagebox.showerror(message=error, title="Erro")

class Agenda:
    def __init__(self) -> None:
        pass

class Programa:
    def __init__(
            self, titulo,
            resizeble = True,
            width = 1920, heigth = 1080
        ) -> None:
        self.janela = Tk()

        self.janela.geometry(f"{width}x{heigth}")
        self.janela.title(titulo)

        self.janela.resizable(resizeble, resizeble)

    def setar_labels(self, nome, size, relx, rely, anchor='center'):
        ttk.Label(self.janela, text=nome, font=("Arial", size)).place(relx=relx, rely=rely, anchor=anchor)

    def setar_inputs(self, size, relx, rely, anchor='center', placeholder=''):
        entry = ttk.Entry(self.janela, font=("Arial", size), show=placeholder)
        entry.place(relx=relx, rely=rely, anchor=anchor)
        return entry

    def setar_button(self, texto, command, relx, rely, anchor='center'):
        ttk.Button(self.janela, text=texto, command=command).place(relx=relx, rely=rely, anchor=anchor)
    
    def iniciar_aplicacao(self):
        self.janela.mainloop()


if __name__ == '__main__':
    programa = Programa(
        titulo="Agenda de Contatos",
        resizeble=False,
        width=640,
        heigth=480
    )

    usuario = Usuario()

    programa.setar_labels('Usuário', 15, 0.5, 0.2)
    username = programa.setar_inputs(15, 0.5, 0.3)
    programa.setar_labels('Senha', 15, 0.5, 0.4)
    password = programa.setar_inputs(size=15, relx=0.5, rely=0.5, anchor='center', placeholder='*')
    programa.setar_button(
        texto='Logar', 
        command=lambda: usuario.setar_login_info(username.get(), password.get()),
        relx=0.5,
        rely=0.6
    )

    programa.iniciar_aplicacao()