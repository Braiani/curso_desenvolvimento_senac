from tkinter import *
from tkinter import ttk

def mudar_cor(cor = ''):
    janela.config(background=cor)

janela = Tk()
janela.title("Botões")
janela.geometry("600x480")



ttk.Button(janela, text='Verde', command=lambda: mudar_cor('green')).place(relx=0.5, rely=0.3, anchor='center')
ttk.Button(janela, text='Azul', command=lambda: mudar_cor('blue')).place(relx=0.5, rely=0.4, anchor='center')
ttk.Button(janela, text='Roxo', command=lambda: mudar_cor('purple')).place(relx=0.5, rely=0.5, anchor='center')

janela.mainloop()