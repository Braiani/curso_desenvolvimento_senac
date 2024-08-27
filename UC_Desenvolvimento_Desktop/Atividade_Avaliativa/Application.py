from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
from SqlHandler import SqlHandler


class Application:
    def __init__(self):
        SqlHandler()
        self.janela = Tk()
        self.images = []
        self.background = 'gray'
        self.title = 'Restaurante do Ederson'

    def set_geometry(self, width, height, center = True, fullscreen = False):
        if fullscreen:
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

    def adicionar_entry(self, relx, rely, anchor, options: dict = {}):
        entrada = ttk.Entry(self.janela)
        if options:
            for key, value in options.items():
                entrada[key] = value
        entrada.place(relx=relx, rely=rely, anchor=anchor)

    def adicionar_label(self, text, relx, rely, anchor, options: dict = {}):
        label = ttk.Label(self.janela, text=text, background=self.background)
        if options:
            for key, value in options.items():
                label[key] = value
        label.place(relx=relx, rely=rely, anchor=anchor)

    def adicionar_button(self, text, relx, rely, anchor, command, options: dict = {}):
        btn = ttk.Button(self.janela, text=text, command=command)
        if options:
            for key, value in options.items():
                btn[key] = value
        btn.place(relx=relx, rely=rely, anchor=anchor)

    def start(self):
        self.janela.mainloop()