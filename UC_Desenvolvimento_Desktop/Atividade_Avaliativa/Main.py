from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Progressbar
from Application import Application
import requests
import tempfile
import threading

class Main(Application):
    def __init__(self, janela: Tk, centered: bool = True):
        super().__init__(janela=janela)
        self.set_geometry(800, 600, centered)
        self.set_title(self.title)
        self.set_background('gray')
        self.images = []
        self.progress_bar = None

    def start(self):
        self.janela.mainloop()
    
    def resize_image(self, image_path: str, width: int, height: int):
        img = PhotoImage(file=image_path)
        if img.width() <= width:
            factor_x = 1
        else:
            factor_x = img.width() / width

        if img.height() <= height:
            factor_y = 1
        else:
            factor_y = img.height() / height

        img = img.subsample(int(factor_x), int(factor_y))
        return img

    def show_progress_bar(self, options):
        if self.progress_bar is None:
            self.progress_bar = Progressbar(self.janela, mode='indeterminate')
            self.progress_bar.place(relx=0.5, rely=0.15, anchor='center', width=self.janela.winfo_screenwidth())
            self.progress_bar.start()
    

    def adicionar_label_image(self, image_url: str, text, options = {}):
        self.show_progress_bar(options=options)

        thread = threading.Thread(target=self.load_image, args=(image_url, text, options))
        thread.start()

    def load_image(self, image_url: str, text, options = {}):
        try:
            get_image = requests.get(image_url)
            get_image.raise_for_status()

            img_data = get_image.content

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(img_data)
                temp_file_path = temp_file.name
            
            img = self.resize_image(image_path=temp_file_path, width=150, height=150)

            self.janela.after(0, self.update_image_label, img, temp_file_path, text, options)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

    def update_image_label(self, img, temp_file_path, text, options):
        if self.progress_bar:
            self.progress_bar.stop()
            self.progress_bar.destroy()
            self.progress_bar = None
        
        self.images.append(img)

        self.adicionar_label(text='', relx=options['relx'], rely=options['rely'],anchor='center', options={
            'image': img
        })

        if 'relx' in options:
            relx = options['relx']
            del(options['relx'])
        
        if 'rely' in options:
            rely = options['rely']
            del(options['rely'])

        self.adicionar_label(text=text, relx=(relx + 0.2), rely=rely, anchor='center', options=options)
        
        self.janela.protocol("WM_DELETE_WINDOW", lambda: self.cleanup(temp_file_path))

    def cleanup(self, file_path):
        import os
        os.remove(file_path)
        self.janela.destroy()