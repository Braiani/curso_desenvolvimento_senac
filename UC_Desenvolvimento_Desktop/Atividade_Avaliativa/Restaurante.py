from tkinter import messagebox
from PIL import Image
from customtkinter import CTk, CTkToplevel
from Main import Main
from Login import Login
from Categoria import Categoria
from Produtos import Produtos
from Splash import Splash
from Cart import Cart


class Restaurante:
    def __init__(self) -> None:
        self.logado = {'name': 'Ederson', 'id': 1}
        # self.logado = None
        self.app_master = None
        self.root = None
        self.shouldLogin = False
        self.cart = None
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

        self.cart = Cart(self.app_master.connector)

        self.app_master.janela.configure(fg_color=self.app_master.get_colors('black'))

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
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'border_color': self.app_master.get_colors('dark_green')
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (0, 30)
                }
            })
            column += 1

        row += 1
        items = self.cart.get_open_cart()
        print(items)
        self.app_master.adicionar_button(text='Carrinho', command=lambda: print('teste'), options={
            'config': {
                'height': 50,
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'border_color': self.app_master.get_colors('dark_green')
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
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'border_color': self.app_master.get_colors('dark_green')
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
        prod_panel.janela.configure(fg_color=prod_panel.get_colors('black'))
        prod_panel.set_geometry(width=1200, height=800, center=True, fullscreen=True)
        prod_panel.set_grid_column_weight(columns=5, weight=1)
        prod_panel.set_row_configure(rows=10, weight=1)
        prod_panel.set_icon()

        prod = Produtos(self.app_master.connector)
        joins = [{
            'table': 'categories',
            'foreing_key': 'category_id',
            'primary_key': 'id'
        }]

        select_join = 'products.id, products.description as produto, products.price as preco, products.image as image, categories.description as categoria'

        produtos = prod.get_all_by_category(category=category_id, join=joins, select_join=select_join)

        # image_background = f"{prod_panel.get_base_path()}/images/background.png"
        # prod_panel.adicionar_label_image(filename=image_background, text='', options={
        #     'config': {
        #         'size': (600,500)
        #     },
        #     'blur': 2,
        #     'grid': {
        #         'row': 0,
        #         'column': 0,
        #         'rowspan': 10,
        #     }
        # })


        frame_title = prod_panel.adicionar_frame(options={
            'config': {
                'width': 100,
                'height': 50,
                'border_width': 2,
                'corner_radius': 32,
                'border_color': prod_panel.get_colors('medium_green'),
                'fg_color': 'transparent',
                'bg_color': 'transparent'
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
                'fg_color': 'transparent'
            },
            'grid': {
                'padx': (50, 50),
                'pady': (10, 5)
            }
        })
        prod_panel.adicionar_label(text=f'Produtos da Categoria {produtos[0]["categoria"]}', master=frame_title, options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'padx': (50,50),
                'pady': (5,10)
            }
        })

        # scrollable = prod_panel.adicionar_frame(master=prod_panel.janela, scrollable=True, options={
        #     'config': {
        #         'width': 800,
        #         'height': 600,
        #         'border_width': 1,
        #         'corner_radius': 32,
        #         'border_color': 'black',
        #         'fg_color': 'transparent',
        #     },
        #     'grid': {
        #         'row': 2,
        #         'column': 1,
        #         'padx': (10, 10),
        #     }
        # })

        row = 2
        column = 0
        for produto in produtos:
            if column == 5:
                column = 0
                row += 1

            text = f"{produto['produto']} - R$ {produto['preco']:.2f}"
            img_file = f"{prod_panel.get_base_path()}/images/{produto['produto']}.png"
            img = Image.open(img_file)

            frame = prod_panel.adicionar_frame(options={
                'config':{
                    'border_width': 2,
                    'corner_radius': 10,
                    'border_color': prod_panel.get_colors('medium_green'),
                    'fg_color': 'transparent',
                },
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (20, 20)
                }
            })


            prod_panel.adicionar_imagem(master=frame, image=img, image_options={
                'config': {
                    'size': (200, 200),
                }
            }, label_options={
                'config': {
                    'text': ''
                },
                'grid': {
                    'row': 0,
                    'column': 0,
                    'pady': (15,0)
                }
            })

            prod_panel.adicionar_label(master=frame, text=text, options={
                'config': {
                    'font': ('Arial', 16),
                    'fg_color': 'transparent'
                },
                'grid': {
                    'row': 1,
                    'column': 0,
                    'pady': (0,0)
                }
            })
            
            cart_image = Image.open(f"{prod_panel.get_base_path()}/images/cart.png")
            prod_panel.adicionar_button(master=frame, text='Adicionar ao Carrinho', command=self.create_add_product_to_cart(produto['id']), options={
                'config': {
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'border_color': prod_panel.get_colors('medium_green'),
                    'image': cart_image
                },
                'grid': {
                    'row': 2,
                    'column': 0,
                    'pady': (0,15)
                }
            })

            column += 1

        back_image = Image.open(f"{prod_panel.get_base_path()}/images/back.png")
        prod_panel.adicionar_button(text='Voltar', command=lambda: self.close_products_window(window=prod_panel), options={
            'config': {
                'corner_radius': 32,
                'fg_color': 'transparent',
                'bg_color': 'transparent',
                'border_color': prod_panel.get_colors('medium_green'),
                'border_width': 2,
                'image': back_image
            },
            'grid': {
                'row': row + 1,
                'column': 0,
                'pady': (20, 20)
            }
        })

        prod_panel.start()

    def create_add_product_to_cart(self, product_id):
        def function():
            self.add_item_to_cart(product_id=product_id)

        return function

    def add_item_to_cart(self, product_id):
        cart = Cart(self.app_master.connector)
        print(cart.get_all())
        print(f"Adicionando item ao carrinho: {product_id}")
        try:
            add_cart = cart.add_item(product_id=product_id, quantity=1)
            if add_cart:
                messagebox.showinfo('Sucesso', 'Produto adicionado ao carrinho!')
            else:
                messagebox.showerror('Erro', 'Erro ao adicionar item ao carrinho!')
        except Exception as e:
            print(f"Erro ao adicionar item ao carrinho: {e}")

    def close_products_window(self, window: Main):
        self.app_master.deiconify()
        window.janela.destroy()

if __name__ == '__main__':
    Restaurante()
