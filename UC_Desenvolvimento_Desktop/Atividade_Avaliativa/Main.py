from tkinter import *
from Application import Application

class Main(Application):
    def __init__(self, janela: Tk, centered: bool = True):
        super().__init__(janela=janela)
        self.set_geometry(800, 600, centered)
        self.set_title('Restaurante do Ederson')
        self.set_background('gray')

    def start(self):
        self.janela.mainloop()

    def abrir_cadastro(self):
        self.janela.destroy()