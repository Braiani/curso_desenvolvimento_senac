from PIL import Image
from customtkinter import CTk, CTkToplevel
from Main import Main
from Login import Login
from Categoria import Categoria
from Produtos import Produtos
from Splash import Splash


class Restaurante:
    def __init__(self) -> None:
        self.logado = {'name': 'Ederson', 'id': 1}
        # self.logado = None
        self.app_master = None
        self.root = None
        self.shouldLogin = False
        self.init()

    def create_show_products(self, categoria_id):
        def function():
            self.show_products(category_id=categoria_id)

        return function

    def init(self):
        temp_ctk = CTk()
        splash = Splash(temp_ctk)
        splash.start()

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
        self.app_master.adicionar_label(text=f'Seja bem vindo {self.logado["name"]}', options={
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

            categoria_id = int(categoria["id"])
            self.app_master.adicionar_button(text=categoria["descricao"], command=self.create_show_products(categoria_id=categoria_id), options={
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

        self.app_master.adicionar_button(text='Sair', command=lambda: self.app_master.close(), options={
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
        prod_panel.set_grid_column_weight(columns=5, weight=1)

        prod = Produtos(self.app_master.connector)
        joins = [{
            'table': 'categories',
            'foreing_key': 'category_id',
            'primary_key': 'id'
        }]

        select_join = 'products.id, products.description as produto, products.price as preco, products.image as image, categories.description as categoria'

        produtos = prod.get_all_by_category(category=category_id, join=joins, select_join=select_join)

        image_background = f"{prod_panel.get_base_path()}/images/background.png"
        prod_panel.adicionar_label_image(filename=image_background, text='', options={
            'config': {
                'size': (1920,1080)
            },
            'blur': 2,
            'background': True,
            'place': {
                'x': 0,
                'y': 0
            }
        })


        frame_title = prod_panel.adicionar_frame(options={
            'config': {
                'width': 300,
                'height': 150,
            },
            'grid': {
                'row': 0,
                'column': 0,
                'columnspan': 5,
                'pady': (10, 5)
            }
        })

        prod_panel.adicionar_label(text=prod_panel.title, master=frame_title, options={
            'config': {
                'font': ('Arial', 32),
            },
            'grid': {
                'padx': (125, 125),
                'pady': (0, 10)
            }
        })
        prod_panel.adicionar_label(text=f'Produtos da Categoria {produtos[0]["categoria"]}', master=frame_title, options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'padx': (125,125),
                'pady': (5,10)
            }
        })


        row = 2
        column = 0
        for produto in produtos:
            if column == 4:
                column = 0
                row += 1

            text = f"{produto['produto']} - R$ {produto['preco']:.2f}"
            img_file = f"{prod_panel.get_base_path()}/images/{produto['produto']}.png"
            img = Image.open(img_file)

            frame = prod_panel.adicionar_frame(options={
                'config':{
                    'width': 120,
                    'height': 120
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (50, 50)
                }
            })


            prod_panel.adicionar_imagem(master=frame, image=img, image_options={
                'config': {
                    'size': (200, 200),
                    'corner_radius': 10,
                }
            }, label_options={
                'config': {
                    'text': ''
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (50, 0)
                }
            })

            prod_panel.adicionar_label(master=frame, text=text, options={
                'config': {
                    'font': ('Arial', 16)
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (150, 0)
                }
            })
            
            cart_image = Image.open(f"{prod_panel.get_base_path()}/images/cart.png")
            prod_panel.adicionar_button(master=frame, text='Adicionar ao Carrinho', command=lambda: print('teste'), options={
                'config': {
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'image': cart_image
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (250, 0)
                }
            })

            column += 1

        back_image = Image.open(f"{prod_panel.get_base_path()}/images/back.png")
        prod_panel.adicionar_button(text='Voltar', command=lambda: self.close_products_window(window=prod_panel), options={
            'config': {
                'corner_radius': 32,
                'fg_color': 'transparent',
                'border_width': 2,
                'image': back_image
            },
            'grid': {
                'row': row + 1,
                'column': 0,
                'pady': (50, 0)
            }
        })

        prod_panel.start()

    def close_products_window(self, window: Main):
        self.app_master.deiconify()
        window.janela.destroy()

if __name__ == '__main__':
    Restaurante()
