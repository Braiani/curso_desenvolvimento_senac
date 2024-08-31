from customtkinter import CTk, CTkToplevel
from Main import Main
from Login import Login
from Categoria import Categoria
from Produtos import Produtos


class Restaurante:
    def __init__(self) -> None:
        self.logado = None
        self.app_master = None
        self.root = None
        self.shouldLogin = True
        self.init()

    def create_show_products(self, categoria_id):
        def function():
            self.show_products(category_id=categoria_id)

        return function

    def init(self):
        if self.shouldLogin and self.logado is None:
            root = CTk()
            login = Login(root)
            login.start()
            self.logado = login.get_logado()
            if not self.logado:
                print('Saindo do programa!')
                exit()

        root = CTk()
        self.root = root
        self.app_master = Main(self.root)

        self.app_master.set_geometry(width=800, height=600, fullscreen=False)
        self.app_master.set_grid_column_weight(columns=3, weight=2)

        self.app_master.adicionar_label(text=self.app_master.title, options={
            'config': {
                'font': ('Arial', 32),
            },
            'grid': {
                'row': 0,
                'column': 1,
            }
        })
        self.app_master.adicionar_label(text=f'Seja bem vindo {self.logado}', options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'row': 1,
                'column': 1,
                'pady': (0,150)
            }
        })

        categorias = Categoria().getAll()
        column = 0
        row = 2

        for categoria in categorias:
            if column == 3:
                column = 0
                row += 1

            categoria_id = int(categoria[0])
            self.app_master.adicionar_button(text=categoria[1], command=self.create_show_products(categoria_id=categoria_id), options={
                'config': {
                    'height': 50,
                    'corner_radius': 10
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (0, 30)
                }
            })
            column += 1

        row += 1
        self.app_master.adicionar_button(text='Carrinho', command=lambda: print('teste'), options={
            'config': {
                'height': 50,
                'corner_radius': 25
            },
            'grid': {
                'row': row,
                'column': 0,
                'pady': (40, 0)
            }
        })

        self.app_master.adicionar_button(text='Sair', command=lambda: print('teste'), options={
            'config': {
                'height': 50,
                'corner_radius': 25
            },
            'grid': {
                'row': row,
                'column': 2,
                'pady': (40, 0)
            }
        })

        self.app_master.start()

    def show_products(self, category_id: int):
        self.app_master.minimize()
        surface = CTkToplevel()
        prod_panel = Main(surface)
        prod_panel.set_geometry(width=600, height=600, center=False, fullscreen=True)

        prod = Produtos(self.app_master.connector)
        joins = [{
            'table': 'categories',
            'foreing_key': 'category_id',
            'primary_key': 'id'
        }]

        produtos = prod.getAllByCategory(category=category_id, join=joins)

        prod_panel.adicionar_label(text=prod_panel.title)
        prod_panel.adicionar_label(text=f'Produtos da Categoria {produtos[0][1]}')

        for produto in produtos:
            text = f"{produto[1]} - R$ {produto[2]:.2f}"
            prod_panel.adicionar_label_image(image_url=produto[4], text=text, options={
                'font': ('Arial', 20)
            })

        prod_panel.adicionar_button(text='Voltar', command=lambda: self.close_products_window(window=prod_panel), options={
            'config': {
                'height': 50,
                'corner_radius': 25
            }
        })

        prod_panel.start()

    def close_products_window(self, window: Main):
        self.app_master.deiconify()
        window.janela.destroy()

if __name__ == '__main__':
    Restaurante()
