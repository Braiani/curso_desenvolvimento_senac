from tkinter import *
from tkinter import messagebox
from Application import Application
from Login import Login

class Main(Application):
    def __init__(self):
        super().__init__()
        self.set_geometry(800, 600)
        self.set_title('Restaurante do Ederson')
        self.set_background('black')
        self.logado = False

        self.adicionar_label('Restaurante do Ederson', 0.5, 0.1, CENTER, {'font': ('Arial', 20), 'foreground': 'white'})
        self.adicionar_button('Cadastro', 0.5, 0.3, CENTER, self.abrir_cadastro)

    def start(self):
        if not self.logado:
            Login().start()
            self.janela.withdraw()

    def abrir_cadastro(self):
        self.janela.destroy()

if __name__ == '__main__':
    try:
        main = Main()
        main.start()
    except Exception as e:
        print(e)
        messagebox.showerror('Erro', 'Ocorreu um erro inesperado!')
        exit()