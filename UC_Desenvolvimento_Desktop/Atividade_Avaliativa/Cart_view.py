import Restaurante
import customtkinter as ctk
from Main import Main
from Cart import Cart
from customtkinter import CTkToplevel
from PIL import Image

class CartView(Main):
    def __init__(self, parent: Restaurante):
        surface = CTkToplevel()
        super().__init__(janela=surface)
        self.parent = parent
        self.cart = Cart(self.connector)
        self.janela.configure(fg_color=self.get_colors('black'))
        self.set_geometry(width=1200, height=800, center=True, fullscreen=False)
        self.set_grid_column_weight(columns=5, weight=2)
        self.set_row_configure(rows=10, weight=1)
        self.set_icon()
        self.set_itens_screen()

    def set_itens_screen(self):
        joins = [{
            'table': 'products',
            'foreing_key': 'product_id',
            'primary_key': 'id'
        }]

        select = 'cart.id, cart.product_id, products.description as produto, products.price as preco'

        itens = self.cart.get_open_cart(join=joins, select_join=select)
        image_background = f"{self.get_base_path()}/images/background.png"
        self.adicionar_label_image(filename=image_background, text='', options={
            'config': {
                'size': (1920,1080)
            },
            'blur': 1,
            'place': {
                'x': 0,
                'y': 0
            }
        })

        frame_title = self.adicionar_frame(options={
            'config': {
                'border_width': 2,
                'corner_radius': 32,
                'border_color': self.get_colors('medium_green'),
                'fg_color': self.get_colors('dark_gray'),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 0,
                'column': 0,
                'columnspan': 5,
                'pady': (10, 5)
            }
        })

        self.adicionar_label(text=self.title, master=frame_title, options={
            'config': {
                'font': ('Arial', 32),
                'fg_color': 'transparent'
            },
            'grid': {
                'padx': (50, 50),
                'pady': (10, 5)
            }
        })
        self.adicionar_label(text='Carrinho', master=frame_title, options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'padx': (50,50),
                'pady': (5,10)
            }
        })

        scrollable_frame = self.adicionar_frame(master=self.janela, scrollable=True, options={
            'config': {
                'width': 1000,
                'height': 400,
                'border_width': 2,
                'corner_radius': 32,
                'border_color': self.get_colors('medium_green'),
                'fg_color': self.get_colors('dark_gray'),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 1,
                'column': 0,
                'columnspan': 5,
                'padx': (5, 5),
                'pady': (5, 5)
            }
        })
        
        if not itens:
            self.adicionar_label(master=scrollable_frame, text='Carrinho Vazio', options={
                'config': {
                    'font': ('Arial', 16),
                    'fg_color': 'transparent'
                },
                'grid': {
                    'row': 0,
                    'column': 0,
                    'columnspan': 5,
                    'padx': (5, 5),
                    'pady': (5, 5)
                }
            })
        else:
            row = 0
            for item in itens:
                print(item)
                img_file = f"{self.get_base_path()}/images/{item['produto']}.png"

                frame = self.adicionar_frame(master=scrollable_frame, options={
                    'config':{
                        'fg_color': 'transparent',
                        'bg_color': '#000001',
                    },
                    'grid': {
                        'row': row,
                        'column': 0,
                        'columnspan': 5,
                        'padx': (30, 30),
                        'pady': (30, 30)
                    }
                })

                self.adicionar_imagem(master=frame, image=Image.open(img_file), image_options={
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
                        'pady': (5, 5)
                    }
                })

                self.adicionar_label(master=frame, text=f"{item['produto']} - R$ {item['preco']:.2f}", options={
                    'config': {
                        'font': ('Arial', 16),
                        'fg_color': 'transparent'
                    },
                    'grid': {
                        'row': 0,
                        'column': 1,
                        'pady': (5, 5)
                    }
                })

                trash_image = Image.open(f"{self.get_base_path()}/images/trash.png")
                self.adicionar_button(master=frame, text='Remover', command=lambda: print('teste'), options={
                    'config': {
                        'corner_radius': 32,
                        'fg_color': 'gray',
                        'border_color': self.get_colors('medium_green'),
                        'border_width': 2,
                        'image': trash_image,
                        'bg_color': '#000001',
                    },
                    'opacity': '#000001',
                    'grid': {
                        'row': 0,
                        'column': 2,
                        'pady': (5, 5)
                    }
                })
                row += 1
        

        back_image = Image.open(f"{self.get_base_path()}/images/back.png")
        self.adicionar_button(text='Voltar', command=lambda: self.close_windows(), options={
            'config': {
                'corner_radius': 32,
                'fg_color': 'transparent',
                'border_color': self.get_colors('medium_green'),
                'border_width': 2,
                'image': back_image,
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 2,
                'column': 0,
                'pady': (20, 20)
            }
        })
        self.adicionar_button(text='Fechar Conta', command=lambda: self.close_windows(), options={
            'config': {
                'corner_radius': 32,
                'fg_color': 'transparent',
                'border_color': self.get_colors('medium_green'),
                'border_width': 2,
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 2,
                'column': 5,
                'pady': (20, 20)
            }
        })

    def close_windows(self):
        self.janela.destroy()
        self.parent.deiconify()

if __name__ == '__main__':
    Restaurante.Restaurante()