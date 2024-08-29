from Main import Main
from Login import Login
from Categoria import Categoria
from Produtos import Produtos
from tkinter import Tk
from tkinter import *
   
class Restaurante:
    def __init__(self) -> None:
        self.logado = 'Felipe'
        self.shouldLogin = False
        self.init()

    def create_show_products(self, categoria_id):
        def function():
            self.showProducts(category_id=categoria_id)
        return function

    def init(self):
        if self.shouldLogin:
            root = Tk()
            app = Login(root)
            app.start()
            self.logado = app.get_logado()
            if not self.logado:
                print('Saindo do programa!')
                exit()
        
        root = Tk()
        app = Main(root)

        app.set_geometry(800, 600, True, True)
        
        app.adicionar_label(text=app.title, relx=0.5, rely=0.05, anchor='center', options={'font': ('Arial', 20), 'foreground': 'white'})
        app.adicionar_label(text=f'Seja bem vindo {self.logado}', relx=0.5, rely=0.1, anchor='center', options={'font': ('Arial', 16), 'foreground': 'white'})
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
                command=self.create_show_products(categoria_id=categoria_id),
                options=btn_options)
            espacamento += 0.05


        app.adicionar_button(text='Carrinho', relx=0.45, rely=espacamento, anchor='center',command=app.janela.quit, options=btn_options)
        app.adicionar_button(text='Sair', relx=0.55, rely=espacamento, anchor='center',command=app.janela.destroy, options=btn_options)
        
        app.start()

    def showProducts(self, category_id: int):
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

        prod_panel.adicionar_label(text=prod_panel.title, relx=0.5, rely=0.05, anchor='center', options={'font': ('Arial', 20), 'foreground': 'white'})
        prod_panel.adicionar_label(text=f'Produtos da Categoria {produtos[0][1]}', relx=0.5, rely=0.1, anchor='center', options=optinos_label)

        espacamento = 0.3
        for produto in produtos:
            text = f"{produto[1]} - R$ {produto[2]:.2f}"
            prod_panel.adicionar_label_image(image_url=produto[4], text=text, options={
                'relx': 0.3,
                'rely': espacamento,
                'anchor': 'center',
                'font': ('Arial', 20)
            })
            espacamento += 0.15
        
        prod_panel.adicionar_button(text='Voltar', relx=0.25, rely=espacamento, anchor='center',command=prod_panel.janela.destroy)

        prod_panel.start()


if __name__ == '__main__':
    Restaurante()