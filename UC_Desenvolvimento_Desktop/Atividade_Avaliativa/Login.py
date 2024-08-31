import customtkinter as ctk
from tkinter import messagebox
from Usuarios import Usuarios
from Main import Main

class Login(Main):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(600, 600, True)
        self.set_title('Login')
        self.set_grid_column_weight(columns=1, weight=3)
        self.entradas = []
        self.logado = False
        self.usuario = None
        self.set_itens_screen()

    def set_itens_screen(self):
        self.adicionar_label_image('https://www.pngkey.com/png/full/114-1149878_setting-user-avatar-in-specific-size-without-breaking.png', 'Login', options={
            'config': {
                'width': 600,
                'height': 600
            },
            'background': True,
            'progress': {
                'position': (0, 590)
            }

        })

        self.adicionar_label(text='Usuário', options={
            'config': {
                'font': ('Arial', 16)
            },
            'grid': {
                'row': 0,
                'pady': (40, 0)
            }
        })
        usuario = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200
            },
            'grid': {
                'row': 1,
                'pady': (5, 0)
            }
        })
        self.entradas.append(usuario)

        self.adicionar_label(text='Senha', options={
            'config': {
                'font': ('Arial', 16)
            },
            'grid': {
                'row': 2,
                'pady': (10, 0)
            }
        })

        senha = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200,
                'show': '*'
            },
            'grid': {
                'row': 3,
                'pady': (5, 0)
            }
        })

        self.entradas.append(senha)

        self.adicionar_label(text='Confirmar Senha', options={
            'config': {
                'font': ('Arial', 16)
            },
            'grid': {
                'row': 4,
                'pady': (10, 0)
            }
        })

        conf_senha = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200,
                'show': '*'
            },
            'grid': {
                'row': 5,
                'pady': (5, 0)
            }
        })

        self.entradas.append(conf_senha)

        self.adicionar_button(text='Entrar', command=lambda: self.validar_login(), options={
            'config': {
                'height': 40,
                'corner_radius': 25
            },
            'grid': {
                'row': 6,
                'pady': (20, 0)
            }
        })

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
    from Restaurante import Restaurante
    Restaurante()