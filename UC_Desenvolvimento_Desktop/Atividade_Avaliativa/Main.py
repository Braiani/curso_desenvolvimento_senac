from customtkinter import CTk
from customtkinter import CTkToplevel
from customtkinter import CTkImage
from customtkinter import CTkLabel
import PIL
from PIL import Image
from customtkinter import CTkProgressBar as Progressbar
from Application import Application
import requests
import tempfile
import threading

class Main(Application):
    def __init__(self, janela: CTk|CTkToplevel, centered: bool = True):
        super().__init__(janela=janela)
        self.set_geometry(800, 600, centered)
        self.set_title(self.title)
        self.images = []
        self.progress_bar = None

    def start(self):
        self.janela.mainloop()

    @staticmethod
    def ctk_image(image_path: Image, size: tuple[int, int]):
        img = CTkImage(image_path, size=size)
        return img


    def show_progress_bar(self, position: tuple[int, int] = (0, 0)):
        if self.progress_bar is None:
            self.progress_bar = Progressbar(self.janela, mode='indeterminate')
            self.progress_bar.configure(width=self.janela.winfo_screenwidth())
            self.progress_bar.place(x=position[0], y=position[1])
            self.progress_bar.start()
    

    def adicionar_label_image(self, image_url: str, text, options=None):
        if options is None:
            options = {}
        if options.get('progress', False):
            position = options['progress'].get('position', (0, 0))
            self.show_progress_bar(position)

        thread = threading.Thread(target=self.load_image, args=(image_url, text, options))
        thread.start()

    def load_image(self, image_url: str, text, options):
        try:
            get_image = requests.get(image_url)
            get_image.raise_for_status()

            img_data = get_image.content

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(img_data)
                temp_file_path = temp_file.name
            img_downloaded = Image.open(temp_file_path)
            img = self.ctk_image(image_path=img_downloaded, size=(500,500))

            self.janela.after(0, self.update_image_label, img, temp_file_path, text, options)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

    def update_image_label(self, img, temp_file_path, text, options):
        if self.progress_bar:
            self.progress_bar.stop()
            self.progress_bar.destroy()
            self.progress_bar = None
        
        self.images.append(img)

        label = CTkLabel(self.janela, image=temp_file_path, text=text)

        self.set_options_elements(options, label)

        label.place(x=0,y=0)
        
        self.janela.protocol("WM_DELETE_WINDOW", lambda: self.cleanup(temp_file_path))

    def cleanup(self, file_path):
        import os
        os.remove(file_path)
        self.janela.destroy()

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()