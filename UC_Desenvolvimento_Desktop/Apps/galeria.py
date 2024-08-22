from tkinter import *
from tkinter import PhotoImage

class Application:
    def __init__(self, options:dict = {}) -> None:
        self.janela = Tk()
        self.images = []
        if 'title' in options:
            self.janela.title(options['title'])
        if 'geometry' in options:
            self.janela.geometry(options['geometry'])
        if 'background' in options:
            self.background = options['background']
            self.janela.config(background=self.background)
    
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

    def container(self, image: dict = {}):
        frame = Frame(self.janela)
        frame.grid(row=image['row'], column=image['col'], padx=30, pady=30)

        img = self.resize_image(image_path=image['src'], width=200, height=200)
        self.images.append(img)

        Label(frame, image=img).pack()
        Entry(frame).pack()

    def start(self):
        self.janela.mainloop()


if __name__ == '__main__':
    options_window = {
        'title': 'Galeria',
        'geometry': '600x600+400+200'
    }
    images = [
        {
            'src': 'C:\\Users\\FelipeSantos\\Documents\\Curso\\UC_Desenvolvimento_Desktop\\Apps\\images\\image1.png',
            'row': 0,
            'col': 0
        },
        {
            'src': 'C:\\Users\\FelipeSantos\\Documents\\Curso\\UC_Desenvolvimento_Desktop\\Apps\\images\\image2.png',
            'row': 0,
            'col': 1
        },
        {
            'src': 'C:\\Users\\FelipeSantos\\Documents\\Curso\\UC_Desenvolvimento_Desktop\\Apps\\images\\image3.png',
            'row': 1,
            'col': 0
        },
        {
            'src': 'C:\\Users\\FelipeSantos\\Documents\\Curso\\UC_Desenvolvimento_Desktop\\Apps\\images\\image4.png',
            'row': 1,
            'col': 1
        },
    ]
    programa = Application(options=options_window)
    
    for image in images:
        programa.container(image)

    programa.start()