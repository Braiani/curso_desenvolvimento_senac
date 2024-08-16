from tkinter import *
from tkinter import ttk

class Usuario:
    def __init__(self, user = '', senha = '') -> None:
        self.user = user
        self.senha = senha
    
    def logar(self):
        try:
            if self.user == '' or self.senha == '':
                raise Exception('Login Inválido')
            
        except Exception as error:
            print(error)


class Agenda:
    def __init__(
            self, titulo,
            resizeble = True,
            width = 1920, heigth = 1080
        ) -> None:
        self.janela = Tk()

        self.janela.geometry(f"{width}x{heigth}")
        self.janela.title(titulo)

        if not resizeble:
            self.janela.resizable(False, False)

        self.frame = ttk.Frame(self.janela)
        self.frame.place(relx=0.5,rely=0.5, anchor='center')
    
    def setar_labels(self, nome, size, column, row):
        ttk.Label(self.frame, text=nome, font=("Arial", size)).grid(column=column, row=row)

    def setar_inputs(self, size, column, row):
        ttk.Entry(self.frame, font=("Arial", size)).grid(column=column, row=row)

    def setar_button(self, texto, size, column, row):
        ttk.Button(self.frame, text=texto).grid(column=column, row=row)
    
    def iniciar_aplicacao(self):
        self.janela.mainloop()


if __name__ == '__main__':
    agenda = Agenda(
        titulo="Agenda de Contatos",
        resizeble=True
    )

    agenda.setar_labels('Usuário', 15, 0,0)
    agenda.setar_inputs(15, 0,1)
    agenda.setar_labels('Senha', 15, 0,2)
    agenda.setar_inputs(15, 0,3)
    agenda.setar_button('Logar', 15, 0,4)

    agenda.iniciar_aplicacao()