from Main import Main
from Login import Login
from Categoria import Categoria
from Produtos import Produtos
from tkinter import Tk
from tkinter import *

logado = 'Felipe'


def showProducts(category_id: int):
    surface = Toplevel()
    prod_panel = Main(surface)
    prod_panel.set_geometry(width=600, height=600, center=False, fullscreen=True)

    prod = Produtos()
    joins = [{
        'table': 'categories',
        'foreing_key': 'category_id',
        'primary_key': 'id'
    }]

    optinos_label = {'font': ('Arial', 16), 'foreground': 'white'}

    produtos = prod.getAllByCategory(category=category_id, join=joins)

    prod_panel.adicionar_label(text='Restaurante do Ederson', relx=0.5, rely=0.05, anchor='center', options={'font': ('Arial', 20), 'foreground': 'white'})
    prod_panel.adicionar_label(text=f'Produtos da Categoria {produtos[0][1]}', relx=0.5, rely=0.1, anchor='center', options=optinos_label)

    espacamento = 0.3
    for produto in produtos:
        prod_panel.adicionar_label(text=f'Produtos {produto[1]}', relx=0.5, rely=espacamento, anchor='center', options=optinos_label)
        espacamento += 0.05

    prod_panel.start()
    



if __name__ == '__main__':
    # root = Tk()
    # app = Login(root)
    # app.start()
    # logado = app.get_logado()
    # if not logado:
    #     print('Saindo do programa!')
    #     exit()
    
    root = Tk()
    app = Main(root)

    app.set_geometry(800, 600, True, True)
    
    app.adicionar_label(text='Restaurante do Ederson', relx=0.5, rely=0.05, anchor='center', options={'font': ('Arial', 20), 'foreground': 'white'})
    app.adicionar_label(text=f'Seja bem vindo {logado}', relx=0.5, rely=0.1, anchor='center', options={'font': ('Arial', 16), 'foreground': 'white'})
    espacamento = 0.3
    btn_options = {
        'padding': 10,
        'width': 25
    }

    categorias = Categoria().getAll()

    for categoria in categorias:
        categoria_id = int(categoria[0])
        app.adicionar_button(
            text=categoria[1],
            relx=0.5,
            rely=espacamento,
            anchor='center',
            command=lambda:showProducts(category_id=categoria_id),
            options=btn_options)
        espacamento += 0.05


    app.adicionar_button(text='Carrinho', relx=0.45, rely=espacamento, anchor='center',command=app.janela.quit, options=btn_options)
    app.adicionar_button(text='Sair', relx=0.55, rely=espacamento, anchor='center',command=app.janela.destroy, options=btn_options)
    
    app.start()