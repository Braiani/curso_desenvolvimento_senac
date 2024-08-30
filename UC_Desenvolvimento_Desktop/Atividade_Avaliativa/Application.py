import customtkinter as ctk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
from SqlHandler import SqlHandler
import os


class Application:
    def __init__(self, janela: ctk.CTk):
        self.connector = SqlHandler()
        self.janela = janela
        self.images = []
        self.buttons = []
        self.background = 'gray'
        self.title = 'Restaurante do Ederson'
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

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

    def adicionar_entry(self, padx, pady, options = {}):
        entrada = ctk.CTkEntry(self.janela)

        entrada.pack(padx=padx, pady=pady)
        return entrada

    def adicionar_label(self, text, padx, pady):
        label = ctk.CTkLabel(self.janela, text=text)
        label.pack(padx=padx, pady=pady)

    def adicionar_button(self, text, padx, pady, command):
        btn = ctk.CTkButton(self.janela, text=text, command=command)
        btn.pack(padx=padx, pady=pady)

        self.buttons.append(btn)

    def start(self):
        self.janela.mainloop()