from tkinter import *
from tkinter import ttk


class Clicador:
    def __init__(self) -> None:
        self.cliques = 0

    def clicou(self):
        self.cliques += 1
        print(f"Você clicou mesmo :o, {self.cliques}")



if __name__ == '__main__':
    janela = Tk()

    width = 640
    heigh = 480
    padding = (heigh / 2) - 20

    frame = ttk.Frame(janela, padding=padding)

    frame.grid()

    janela.geometry(f"{width}x{heigh}")

    clicador = Clicador()

    ttk.Label(frame, text="Olá Mundo", font=("Arial", 30)).grid(column=0, row=0)
    ttk.Button(frame, text="Clique se for capaz!", width=50, padding=20, command=clicador.clicou).grid(column=0, row=1)
    janela.mainloop()