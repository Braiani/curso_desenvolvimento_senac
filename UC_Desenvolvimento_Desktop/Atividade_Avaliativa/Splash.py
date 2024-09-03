import customtkinter as ctk
import PIL
from PIL import Image
from Main import Main
import os, sys
from Produtos import Produtos
import threading
import requests


class Splash(Main):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(350, 280, True)
        self.set_title('Splash')
        self.set_grid_column_weight(columns=1, weight=3)

        self.adicionar_imagem(image=self.get_icon(), image_options={
            'config': {
                'size': (200, 200)
            }
        }, label_options={
            'grid': {
                'pady': (10, 0)
            }
        })

        self.adicionar_label(text='Carregando...', options={
            'config': {
                'font': ('Arial', 16)
            },
            'grid': {
                'row': 1,
                'pady': (5, 0)
            }
        })

        self.progressbar = self.adicionar_progressbar(options={
            'grid': {
                'row': 2,
                'pady': (5, 0)
            }
        })

        thread = threading.Thread(target=self.check_and_download_images)
        thread.start()

        self.janela.protocol("WM_DELETE_WINDOW", self.on_closing)

    def check_and_download_images(self):
        try:
            path = os.path.dirname(os.path.abspath(sys.argv[0]))
            if not os.path.isdir(f"{path}/images"):
                os.mkdir(f"{path}/images")

            produtos = Produtos(self.connector)
            produtos = produtos.get_all()
            total_produtos = len(produtos)

            list_imagens_download_avulsas = {
                'Login': 'https://blogmaladeviagem.com.br/wp-content/uploads/2019/10/Fogo-caipira-2.png',
                # 'background': 'https://images.unsplash.com/photo-1605926637512-c8b131444a4b?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'background': 'https://i.pinimg.com/736x/ce/1a/18/ce1a18dcf0c6cfc9b5538dfae8e4aa09.jpg',
                'cart': 'https://www.clker.com//cliparts/j/s/U/7/a/W/shopping-cart-hi.png',
                'back': 'https://cdn-icons-png.flaticon.com/512/5548/5548528.png'
            }

            increment_value = (100/(total_produtos + len(list_imagens_download_avulsas))) / 2
            self.increment_progressbar(increment_value)

            for key, value in list_imagens_download_avulsas.items():
                filename = f"{path}/images/{key}.png"
                if not os.path.isfile(filename):
                    self.download_save(value, filename)
                    self.step_progressbar()

            for produto in produtos:
                self.step_progressbar()
                filename = f"{path}/images/{produto['description']}.png"
                if not os.path.isfile(filename):
                    self.download_save(produto['image'], filename)

            self.janela.after(0, self.close_window)
        except Exception as e:
            print(f"Erro ao carregar as imagens: {e}")
            self.janela.after(0, self.close_window)

    @staticmethod
    def download_save(url, filename):
        try:
            get_image = requests.get(url)
            get_image.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(get_image.content)
            return True
        except Exception as e:
            print(f"Erro ao fazer download da image: {e}")
            raise Exception(e)


    def step_progressbar(self):
        self.progressbar.step()

    def stop_progressbar(self):
        self.progressbar.stop()

    def increment_progressbar(self, value):
        self.progressbar.configure(determinate_speed=value)

    @staticmethod
    def get_icon():
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        filename = f"{path}/icon.png"
        img = Image.open(filename)
        return img

    def close_window(self):
        self.progressbar.stop()
        self.janela.destroy()

    def on_closing(self):
        self.janela.destroy()

    def start(self):
        self.janela.mainloop()

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()