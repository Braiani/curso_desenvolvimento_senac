from Main import Main
from Login import Login
from tkinter import Tk

logado = False

if __name__ == '__main__':
    root = Tk()
    app = Login(root)
    app.start()
    logado = app.get_logado()
    if not logado:
        print('Saindo do programa!')
        exit()
    
    root = Tk()
    app = Main(root)

    app.set_geometry(800, 600, True, True)
    
    app.adicionar_label('Restaurante do Ederson', 0.5, 0.1, 'center', {'font': ('Arial', 20), 'foreground': 'white'})
    app.adicionar_label(f'Seja bem vindo {logado}', 0.5, 0.2, 'center', {'font': ('Arial', 16), 'foreground': 'white'})
    app.adicionar_button('Cadastro', 0.5, 0.3, 'center', app.abrir_cadastro)
    app.adicionar_button('Sair', 0.5, 0.4, 'center', app.janela.quit)
    
    app.start()